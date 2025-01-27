import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
num = list(map(int, input().split()))
num.sort()
start, end = 0, N-1
cnt = 0

while start < end:
    if num[start] + num[end] < M:
        start += 1
    elif num[start] + num[end] > M:
        end -= 1
    elif num[start] + num[end] == M:
        start += 1
        cnt += 1

print(cnt)