init = int(input())
num = init
cycle = 0

while num != init or cycle == 0:
    old_tens = num // 10
    old_ones = num % 10

    new_num = old_ones + old_tens
    new_ones = new_num % 10

    num = old_ones * 10 + new_ones
    cycle +=1

print(cycle)