import sys
input = sys.stdin.readline

L = []

for i in range(9):
    n = int(input())
    L.append(n)

res = max(L)
result = L.index(res)

print(res, result + 1, sep='\n')