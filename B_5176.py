T = int(input())

S = set()

for i in range(T):
    P, M = map(int, input().split())
    for j in range(P):
        N = int(input())
        S.add(N)

    print(P - len(S))
    S = set()