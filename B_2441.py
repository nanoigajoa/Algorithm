N = int(input())

for i in range(N, 0, -1):
    print('{0:>{1}}'.format('*' * i, N))