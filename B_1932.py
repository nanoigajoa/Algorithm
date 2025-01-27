import sys
input = sys.stdin.readline

n = int(input())
trg = [list(map(int, input().split())) for _ in range(n)]
print(trg)

dp = [[0]*(i+1) for i in range(n)]
dp[0] = trg[0]
print(dp)