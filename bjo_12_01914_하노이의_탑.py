def move(n, start, end):
    print(f'{start} {end}')
    return

def hanoi(n, start, end, sub):
    if n == 1:
        move(n=1, start=start, end=end)
        return

    else:
        hanoi(n-1, start=start, end=sub, sub=end)
        move(n, start=start, end=end)
        hanoi(n-1, start=sub, end=end, sub=start)

n = int(input())
print(f'{2**n - 1}')

if n <= 20:
    hanoi(n, '1', '3', '2')