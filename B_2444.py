N = int(input())

for i in range(1, N + 1):
    line = '{:^{width}}'.format('*' * (2 * i - 1), width=N * 2 - 1)
    print(line.rstrip())

for i in range(N - 1, 0, -1):
    line = '{:^{width}}'.format('*' * (2 * i - 1), width=N * 2 - 1)
    print(line.rstrip())
