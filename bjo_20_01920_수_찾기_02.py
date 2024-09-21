import sys

def binary_search(lst, target):
    left, right = 0, len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return True
        elif lst[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False


N = int(input())
A = sorted(list(map(int, sys.stdin.readline().split())))

M = int(input())
targets = list(map(int, sys.stdin.readline().split()))

for target in targets:
    print(1 if binary_search(A, target) else 0)