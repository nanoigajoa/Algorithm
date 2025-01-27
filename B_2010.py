# N = int(input())
# result = 1

# for i in range(N):
#     n = int(input())
#     result += n - 1

# print(result)
# ------------------

import sys
n = sys.stdin.readline

N = int(input())
result = 1

for i in range(N):
    n = int(input())
    result += n - 1

print(result)