import telebot
from telebot import types
from datetime import datetime
import os

BOT_TOKEN = os.getenv("tg_bot")

bot = telebot.TeleBot(BOT_TOKEN)

user_sleep_data = {}

sleep_start_times = {}

aaaaaAAAAAAAAAAA
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я бот для отслеживания сна. Используй /help для списка команд.")


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message,
                 "Команды:\n"
                 "/start - начать\n"
                 "/sleep - отметить начало сна\n"
                 "/wake - отметить конец сна и получить продолжительность сна\n"
                 "/set <уровень сна> - установить уровень сна\n"
                 "/notes <заметки> - добавить заметки ко сну\n"
                 "/get_last - получить последнюю запись о сне"
                 )


@bot.message_handler(commands=['sleep'])
def set_sleep_start(message):
    user_id = message.from_user.id
    if user_id in sleep_start_times:
        bot.reply_to(message,
                     "Вы уже отметили начало сна! Используйте /wake для отметки конца сна")
    else:
        sleep_start_times[user_id] = datetime.now()
        bot.reply_to(message, "Спокойной ночи! Я засек начало твоего сна.")


@bot.message_handler(commands=['wake'])
def set_sleep_end(message):
    user_id = message.from_user.id
    if user_id not in sleep_start_times:
        bot.reply_to(message,
                     "Сначала отметьте начало сна командой /sleep.")
        return

    start_time = sleep_start_times.pop(user_id)
    end_time = datetime.now()
    duration = end_time - start_time
    duration_seconds = duration.total_seconds()

    if user_id not in user_sleep_data:
        user_sleep_data[user_id] = []
    user_sleep_data[user_id].append({
        'start_time': start_time,
        'duration': duration_seconds,
        'quality': None,
        'notes': None})

    hours = int(duration_seconds // 3600)
    minutes = int((duration_seconds % 3600) // 60)
    seconds = int(duration_seconds % 60)

    bot.reply_to(message,
                 f"Доброе утро! Вы спали {hours} часов {minutes} минут {seconds} секунд. "
                 f"Теперь можно установить уровень сна через /set и добавить заметки через /notes.")


@bot.message_handler(commands=['set'])
def set_sleep_quality(message):
    user_id = message.from_user.id
    args = message.text.split()[1:]

    if not args:
        bot.reply_to(message,
                     "Пожалуйста, укажите уровень сна после команды (например: /set 5).")
        return

    try:
        quality = args[0]
        if user_id not in user_sleep_data or not user_sleep_data[user_id]:
            bot.reply_to(message,
                         "Сначала отметьте время сна с помощью /sleep и /wake."
                         )
            return
        user_sleep_data[user_id][-1]['quality'] = quality
        bot.reply_to(message, f"Уровень сна установлен: {quality}")
    except (ValueError, IndexError):
        bot.reply_to(message,
                     "Уровень сна должен быть числом (например: /set 5).")


@bot.message_handler(commands=['notes'])
def add_sleep_notes(message):
    user_id = message.from_user.id
    args = message.text.split()[1:]
    notes = " ".join(args)

    if not notes:
        bot.reply_to(message,
                     "Пожалуйста, укажите заметки после команды (например: /notes спал плохо).")
        return

    if user_id not in user_sleep_data or not user_sleep_data[user_id]:
        bot.reply_to(message,
                     "Сначала отметьте время сна с помощью /sleep и /wake.")
        return

    user_sleep_data[user_id][-1]['notes'] = notes
    bot.reply_to(message, f"Заметки добавлены: {notes}")


@bot.message_handler(commands=['get_last'])
def get_last_sleep_data(message):
    user_id = message.from_user.id
    if user_id not in user_sleep_data or not user_sleep_data[user_id]:
        bot.reply_to(message,
                     "Нет данных о вашем сне. Используйте /sleep, /wake, /set и /notes.")
        return

    last_sleep_data = user_sleep_data[user_id][-1]
    start_time_str = last_sleep_data['start_time'].strftime('%Y-%m-%d %H:%M:%S')
    duration_hours = int(last_sleep_data['duration'] // 3600)
    duration_minutes = int((last_sleep_data['duration'] % 3600) // 60)
    duration_seconds = int(last_sleep_data['duration'] % 60)

    response = (f"Время начала: {start_time_str}\n"
                f"Продолжительность: {duration_hours} часов {duration_minutes} минут {duration_seconds} секунд\n"
                f"Уровень сна: {last_sleep_data['quality']}\n"
                f"Заметки: {last_sleep_data['notes']}")

    bot.reply_to(message, response)


if __name__ == '__main__':
    bot.polling(none_stop=True)
