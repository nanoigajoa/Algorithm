import sys
input = sys.stdin.readline

N = int(input())
count = 0

score = [int(input()) for _ in range(N)]
score = score[::-1]
# print(score)

score_set = set(score)

if len(score_set) == 1:
    for i in range(N):
        score[i] -= i
        count += i
else:
    for i in range(len(score) - 1):
        if score[i + 1] >= score[i]:
            difference = score[i + 1] - score[i] + 1
            score[i + 1] -= difference 
            count += difference
            difference = 0

print(count)

# 다른사람꺼 (신기함)
# n = int(input())
# score = list(int(input()) for _ in range(n))

# ans = 0
# cur = score[n-1]
# for i in reversed(range(n-1)):
#     cur = min(cur - 1, score[i])
#     ans += max(score[i] - cur, 0)

# print(ans)

