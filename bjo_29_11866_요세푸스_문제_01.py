def josephus(n: int, k: int) -> list[int]:
    res: list[int] = []
    line: list[int] = [1 for _ in range(n)] #값이 1이면 제거 대상, 0이면 제거 완료
    i: int = -1
    for _ in range(n-1):
        count: int = 0
        while count < k:
            i = (i + 1) % n #계속 순환하므로 나머지 연산으로 인덱스 계산
            if line[i]:     #제거된 것이 아닐 때만 count 증가
                count += 1
        line[i] = 0
        res.append(i+1)

    res.append(line.index(1)+1)
    return res


#테스트 코드
print(josephus(10, 7))
