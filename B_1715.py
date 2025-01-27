import sys
input = sys.stdin.readline

N = int(input())
bundle = [int(input()) for _ in range(N)]
bundle.sort()
# print(bundle)
next = 0

for i in range(N - 1):
    if next == 0:
        next += bundle[i] + bundle[i + 1]
    else:
        next += next + bundle[i + 1]

print(next)