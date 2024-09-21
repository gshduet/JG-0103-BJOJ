from collections import deque


def josephus_deque(n: int, k: int) -> list[int]:
    q = deque(range(1, n + 1))
    res = []

    while len(q) > 1:
        q.rotate(-(k - 1))
        res.append(q.popleft())

    res.append(q[0])
    return res


# 테스트 코드
print(josephus_deque(10, 7))