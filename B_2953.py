import sys
input = sys.stdin.readline

S = []
  
for i in range(5):
    point = list(map(int, input().split()))
    S.append(sum(point))

result = max(S)

print(S.index(result) + 1, result, sep=' ')