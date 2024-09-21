class Stack:
    def __init__(self):
        self.lst = []
        self.length = 0

    def push(self, value):
        self.lst.append(value)
        self.length += 1

    def pop(self):
        if self.length:
            self.length -= 1
            return self.lst.pop()

        return None

    @property
    def size(self):
        return self.length

    @property
    def empty(self):
        return 1 if not self.length else 0

    def top(self):
        if self.length:
            return self.lst[-1]

        return None


def calculate_bracket_value(brackets: str) -> int:
    stack = Stack()

    for char in brackets:
        match char:
            case '(' | '[':
                stack.push(char)
            case ')' | ']':
                temp_sum = 0

                while not stack.empty and isinstance(stack.top(), int):
                    temp_sum += stack.pop()

                if stack.empty:
                    return 0

                opening_bracket = stack.pop()

                match (opening_bracket, char):
                    case ('(', ')'):
                        value = 2 if temp_sum == 0 else 2 * temp_sum
                    case ('[', ']'):
                        value = 3 if temp_sum == 0 else 3 * temp_sum
                    case _:
                        return 0

                stack.push(value)

    result = 0

    while not stack.empty:
        top = stack.pop()

        if not isinstance(top, int):
            return 0

        result += top

    return result

bracket_string = input()
print(calculate_bracket_value(bracket_string))