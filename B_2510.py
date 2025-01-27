N, K = map(int, input().split())
yak = []
for i in range(1, N + 1):
    if N % i == 0:
        yak.append(i)

if K <= len(yak):
    print(yak[K-1])
else:
    print(0)