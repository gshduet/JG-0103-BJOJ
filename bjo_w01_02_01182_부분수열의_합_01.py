import sys
from itertools import combinations

nums, target = list(map(int, sys.stdin.readline().split()))
number_list = list(map(int, sys.stdin.readline().split()))

combi_list = []
answer = 0

for i in range(1, nums+1):
    for combi in list(combinations(number_list, i)):
        if sum(combi) == target:
            answer += 1

print(answer)
