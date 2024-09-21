import sys

nums, target = map(int, sys.stdin.readline().split())
number_list = list(map(int, sys.stdin.readline().split()))

def dfs(n, sum, cnt):
    answer = 0

    if n >= nums:
        if sum == target and cnt > 0:
            answer += 1

        return

    dfs(n + 1, sum + number_list[n], cnt + 1)
    dfs(n + 1, sum, cnt)

    return answer


dfs(0, 0, 0)
print(dfs())