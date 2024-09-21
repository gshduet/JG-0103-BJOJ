import sys

input_list = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]

for value in sorted(input_list):
    print(value)