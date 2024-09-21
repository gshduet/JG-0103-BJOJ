import sys

def find_max_height(trees, target):
    left, right = 0, max(trees)

    while left <= right:
        mid = (left + right) // 2
        cut = sum(tree - mid if tree > mid else 0 for tree in trees)

        if cut >= target:
            left = mid + 1
        else:
            right = mid - 1

    return right


input = sys.stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().split()))

print(find_max_height(trees, M))