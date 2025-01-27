# import sys
# input = sys.stdin.readline

# N = int(input())
# count = 0

# while True:
#     if N == 1:
#         break

#     if N % 3 == 0: #3으로 나눠질 경우
#         N = N // 3

#     elif N % 3 == 1:
#         N = N - 1

#     elif N % 2 == 0: #2로 나눠질 경우
#         N = N // 2

#     count += 1
#     print(N)

# print(count)

import sys
input = sys.stdin.readline

N = int(input().strip())
dp = [0] * (N + 1)

for i in range(2, N + 1):
    # 1을 빼는 경우
    dp[i] = dp[i - 1] + 1
    
    # 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    
    # 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

# 결과 출력
# print(dp)
print(dp[N])
