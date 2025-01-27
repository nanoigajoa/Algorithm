import sys
input = sys.stdin.readline

N = int(input())
L = [int(input()) for _ in range(N)]

positive = []
negative = []
ones = 0
zeros = 0

for num in L:
    if num > 1:
        positive.append(num)
    elif num == 1:
        ones += 1
    elif num == 0:
        zeros += 1
    else:
        negative.append(num)

positive.sort(reverse=True)
negative.sort()

result = 0

# 큰 양수들 묶기
for i in range(0, len(positive) - 1, 2):
    result += max(positive[i] * positive[i + 1], positive[i] + positive[i + 1])
if len(positive) % 2 == 1:
    result += positive[-1]

# 작은 음수들 묶기
for i in range(0, len(negative) - 1, 2):
    result += negative[i] * negative[i + 1]
if len(negative) % 2 == 1:
    if zeros > 0:
        result += 0  # 음수가 홀수개이고 0이 있는 경우
    else:
        result += negative[-1]

# 1 더하기
result += ones

print(result)
