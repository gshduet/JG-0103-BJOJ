def move(n, start, end):
    print(f'{n}번 원반을 {start}에서 {end}로 이동')

def hanoi(n, start, end, sub):
    if n == 1:
        move(n=1, start=start, end=end)
        return
    else:
        hanoi(n-1, start=start, end=sub, sub=end)
        move(n, start=start, end=end)
        hanoi(n-1, start=sub, end=end, sub=start)

hanoi(5, 'A', 'C', 'B')
