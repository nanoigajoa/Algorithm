import sys
input = sys.stdin.readline

N = int(input())

L = set()

for _ in range(N):
    L.add(input().rstrip())

L = list(L)

L.sort(key=lambda x: (len(x), x))

for i in L:
    print(i)