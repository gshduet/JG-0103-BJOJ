# 팩토리얼은 애초에 자연수라는 범위 안에서의 개념이므로 음수, 0 따위는 생각하지 말 것

def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n-1)
