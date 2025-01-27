import sys
input = sys.stdin.readline

N = int(input().strip())
seq = [int(input().strip()) for _ in range(N)]

stack = []
result = []
current = 1
idx = 0

while current <= N:
    stack.append(current)
    result.append('+')
    current += 1

    while stack and stack[-1] == seq[idx]:
        stack.pop()
        result.append('-')
        idx += 1

if stack:
    print('NO')
else:
    for res in result:
        print(res)
