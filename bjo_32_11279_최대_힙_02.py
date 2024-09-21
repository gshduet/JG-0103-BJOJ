import sys
import heapq

heap = []

commands = [int(sys.stdin.readline()) for _ in range(int(input()))]

for command in commands:
    if command == 0:
        if heap:
            print(-heapq.heappop(heap))

        else:
            print(0)

    else:
        heapq.heappush(heap, -command)