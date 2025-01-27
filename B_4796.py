import sys
input = sys.stdin.readline

i = 0
while True:
    result = 0
    i += 1
    L, P, V = map(int, input().split())

    if L == 0 and P == 0 and V == 0:
        break

    a = V // P # 2
    b = a * L # 10
    result += b + min(L, (V - (P*a)))
    print(L)
    print(V - (P*a))

    print(f"Case {i}: {result}")