N = int(input())
height = list(map(int, input().split()))
stack = []
result = [0] * N

for i in range(N-1, -1, -1): # i = 43210
    while stack and height[stack[-1]] < height[i]:
        result[stack.pop()] = i + 1
    stack.append(i)

print(*result)