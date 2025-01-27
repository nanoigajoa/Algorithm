import sys
input = sys.stdin.readline

N = int(input())
count = 0

for _ in range(N):
    S = input().rstrip()
    stack = []

    for i in range(len(S)):
        if stack:
            if S[i] == stack[-1]: # 이미 있을 때
                stack.pop()
            else:  # 맨처음
                stack.append(S[i])
        else:
            stack.append(S[i])

    if not stack:
        count += 1

print(count)
