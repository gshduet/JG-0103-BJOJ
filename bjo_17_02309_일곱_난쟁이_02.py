import sys

heights = [int(sys.stdin.readline()) for _ in range(9)]

total = sum(heights)

for i in range(8):
    for j in range(i + 1, 9):
        if total - heights[i] - heights[j] == 100:
            result = [h for k, h in enumerate(heights) if k != i and k != j]

            for h in sorted(result):
                print(h)
