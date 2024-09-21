def prime_num_list(n: int) -> list:
    if n <= 2:
        return []

    sieve = [True] * (n - 1)

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i - 2]:
            for j in range(i * i, n, i):
                sieve[j - 2] = False

    return [num for num in range(2, n) if sieve[num - 2]]

input_list = [int(input()) for _ in range(int(input()))]

primes = prime_num_list(max(input_list))

for target in input_list:
    a = b = target // 2

    while a > 0:
        if a in primes and b in primes:
            print(f'{a} {b}')

            break
        else:
            a -= 1
            b += 1
