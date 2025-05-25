class Task:
    def __init__(self, name):
        self.name = name


class TaskQueue:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_next_task(self):
        if not self.is_empty():
            return self.tasks.pop(0)
        else:
            return None

    def is_empty(self):
        return not self.tasks


if __name__ == "__main__":
    queue = TaskQueue()

    task1 = Task("Задача 1")
    task2 = Task("Задача 2")
    task3 = Task("Задача 3")

    queue.add_task(task1)
    queue.add_task(task2)
    queue.add_task(task3)

    next_task = queue.get_next_task()
    print(f"Следующая задача: {next_task.name if next_task else 'Нет задач'}")

    queue.get_next_task()

    print(f"Очередь пуста: {queue.is_empty()}")

    next_task = queue.get_next_task()
    print(f"Следующая задача: {next_task.name if next_task else 'Нет задач'}")

    next_task = queue.get_next_task()
    print(f"Следующая задача: {next_task.name if next_task else 'Нет задач'}")

    print(f"Очередь пуста: {queue.is_empty()}")
