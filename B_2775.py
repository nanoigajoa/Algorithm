import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    dp = [[0]*n] * (k+1) #1호는 인덱스 0
    dp[0] = list(range(1,n+1))

    for i in range(1,k+1):
        for j in range(n):
            if j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

    print(dp[k][n-1])
