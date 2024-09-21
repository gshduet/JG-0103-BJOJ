from collections import deque
from sys import stdin

class Queue:
    def __init__(self):
        self.lst = deque()

    def push(self, value: int):
        self.lst.append(value)

    def pop(self):
        if self.lst:
            return self.lst.popleft()
        return -1

    def size(self):
        return len(self.lst)

    def empty(self):
        return 1 if not self.lst else 0

    def front(self):
        if self.lst:
            return self.lst[0]
        return -1

    def back(self):
        if self.lst:
            return self.lst[-1]
        return -1


commands = [stdin.readline().split() for _ in range(int(input()))]
q = Queue()

for command in commands:
    if command[0] == 'push':
        q.push(int(command[1]))

    elif command[0] == 'pop':
        print(q.pop())

    elif command[0] == 'size':
        print(q.size())

    elif command[0] == 'empty':
        print(q.empty())

    elif command[0] == 'front':
        print(q.front())

    elif command[0] == 'back':
        print(q.back())