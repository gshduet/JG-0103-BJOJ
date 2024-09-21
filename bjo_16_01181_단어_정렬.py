import sys

input_list = [sys.stdin.readline().strip() for _ in range(int(input()))]
input_list = sorted(list(set(input_list)))

for v in sorted(input_list, key=len):
    print(v)