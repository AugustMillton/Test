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


def is_valid_parentheses(s):
    stack = Stack()
    matching_pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.is_empty():
                return False
            top_element = stack.pop()
            if top_element != matching_pairs.get(char):
                return False

    return stack.is_empty()


parentheses_sequence = input("Введите скобочную последовательность: ")

if is_valid_parentheses(parentheses_sequence):
    print("Строка является правильной скобочной последовательностью.")
else:
    print("Строка не является правильной скобочной последовательностью.")
