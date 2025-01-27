import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 1

for num in arr:
    if result < num:
        break

    result += num

print(result)