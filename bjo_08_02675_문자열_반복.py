import sys

sinput = sys.stdin.readline

t = int(sinput())

for _ in range(t):
    R, S = sinput().split()
    R = int(R)
    P = ''.join(char * R for char in S.strip())

    print(P)