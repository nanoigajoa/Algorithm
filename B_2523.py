N = int(input())

for i in range(1, N + 1):
    line = '{:<{width}}'.format('*' * i, width=N)
    print(line.rstrip())

for i in range(N - 1, 0, -1):
    line = '{:<{width}}'.format('*' * i, width=N)
    print(line.rstrip())

