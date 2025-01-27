import sys
input = sys.stdin.readline

N = int(input())
dasom = int(input())
voter = [int(input().rstrip()) for i in range(N - 1)]
voter.sort(reverse=True)
count = 0

if N == 1:
    print(0)
else:
    while voter[0] >= dasom:
        dasom += 1
        voter[0] -= 1
        count += 1
        voter.sort(reverse=True)

    print(count)