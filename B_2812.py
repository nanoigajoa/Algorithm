import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num = list(input().rstrip())

stack = []

for i in num:
    while stack and K > 0 and stack[-1] < i:
        stack.pop()
        K -= 1
    stack.append(i)

if K > 0:
    stack = stack[:-K]

print("".join(stack))
