import sys

input = sys.stdin.readline

input()
valid_set = set(map(int, input().split()))
input()

for num in map(int, input().split()):
    print(1 if num in valid_set else 0)