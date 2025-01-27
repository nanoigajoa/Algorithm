import sys
input = sys.stdin.readline

T = int(input())
list = [int(input()) for _ in range(T)]
count = 0

money = [25, 10, 5, 1]

for l in list:
    result = []
    for mone in money:
        count += l // mone
        l %= mone
        result.append(count)
        count = 0
    print(*result)