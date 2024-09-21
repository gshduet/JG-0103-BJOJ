import sys

class Stack:
    def __init__(self):
        self.lst = []
        self.length = 0

    def push(self, value: int):
        self.lst.append(int(value))
        self.length += 1

    def pop(self):
        if self.length:
            self.length -= 1
            return self.lst.pop()

        return None

    def size(self):
        return self.length

    def empty(self):
        return 1 if not self.length else 0

    def top(self):
        if self.length:
            return self.lst[-1]

        return None

stack = Stack()
cases = int(sys.stdin.readline())

for _ in range(cases):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        stack.push(command[1])

    elif command[0] == 'pop':
        print(stack.pop())

    elif command[0] == 'size':
        print(stack.size())

    elif command[0] == 'empty':
        print(stack.empty())

    elif command[0] == 'top':
        print(stack.top())