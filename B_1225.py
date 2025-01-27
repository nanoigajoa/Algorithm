import sys
input = sys.stdin.readline

S = input().split()
final = 0

S1 = [int(c) for c in S[0]]
S2 = [int(c) for c in S[1]]
result = [S1, S2]
sum = sum(result[1])

for i in range(len(result[0])):
    final += (sum * result[0][i])

print(final)