from itertools import combinations

dwarves = sorted([int(input()) for _ in range(9)])

for v in combinations(dwarves, 7):
    if sum(v) == 100:
        print(*v, sep='\n')

        break
