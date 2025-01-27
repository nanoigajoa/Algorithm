import sys
input = sys.stdin.readline

N = int(input()) # 계단 개수
scores = [0] * N
dp = [0] * N

for i in range(N):
    scores[i] = int(input())

dp[0] = scores[0]
if N > 1:
    dp[1] = scores[0] + scores[1]

for j in range(2, N):
    dp[j] = max(dp[j-2] + scores[j], dp[j-3] + scores[j-1] + scores[j])

print(dp[N-1])
print(dp)
print(scores)