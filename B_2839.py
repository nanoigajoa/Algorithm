N = int(input())
share = 0

while N >= 0:
    if N % 5 == 0:
        share += N // 5
        print(share)
        break
    N -= 3
    share += 1
else:
    print(-1)