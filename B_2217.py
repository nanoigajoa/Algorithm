import sys
input = sys.stdin.readline

N = int(input())
Rope = [int(input()) for _ in range(N)]
Rope.sort()
result = []

for i in range(len(Rope)):
    norm = Rope[i] * (len(Rope) - i)
    if Rope[-1] > norm:
        result.append(Rope[-1])
    else:
        result.append(norm)

result.sort()
print(result[-1])
