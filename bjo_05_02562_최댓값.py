count = 0
answer = 0

for i in range(9):
    tmp = int(input())

    if tmp > answer:
        answer = tmp
        count = i+1

    else:
        continue

print(answer)
print(count)