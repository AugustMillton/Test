class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Стек пуст")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Стек пуст")


def evaluate_rpn(expression):
    global result
    stack = Stack()
    tokens = expression.split()

    for token in tokens:
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            stack.push(int(token))
        elif token in "+-*/":
            if stack.is_empty():
                return "Ошибка: Недостаточно операндов"
            operand2 = stack.pop()
            if stack.is_empty():
                return "Ошибка: Недостаточно операндов"
            operand1 = stack.pop()

            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                if operand2 == 0:
                    return "Ошибка: Деление на ноль"
                result = operand1 / operand2
            stack.push(result)
        else:
            return "Ошибка: Недопустимый токен"

    if stack.is_empty():
        return "Ошибка: Пустое выражение"

    final_result = stack.pop()
    if not stack.is_empty():
        return "Ошибка: Слишком много операндов"

    return final_result


rpn_expression = input("Введите выражение в обратной польской записи: ")
result = evaluate_rpn(rpn_expression)
print("Результат:", result)
