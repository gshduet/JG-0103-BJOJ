# def search_prime(n):
#     answer = 0
#
#     sieve = [True] * (n + 1)
#     sieve[0] = False
#     sieve[1] = False
#
#     for i in range(2, int(n ** 0.5) + 1):
#         if sieve[i]:
#             for j in range(2 * i, n + 1, i):
#                 if sieve[j]:
#                     sieve[j] = False
#
#     return answer


def count_primes(numbers):
    max_num = max(numbers)
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(max_num ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False

    return sum(sieve[num] for num in numbers)


# 입력 처리
N = int(input())
numbers = list(map(int, input().split()))

# 결과 출력
print(count_primes(numbers))