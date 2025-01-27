import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
array.sort()
x = int(input())
cnt = 0
start, end = 0, n-1

while start < end:
    if array[start] + array[end] == x:
        cnt += 1
        start += 1
        end -= 1
    elif array[start] + array[end] < x:
        start += 1
    else:
        end -= 1
print(cnt)