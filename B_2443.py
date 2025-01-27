N = int(input())

for i in range(N, 0, -1):
    result = ('{0:^{width}}'.format('*' * (2*i-1), width = N*2-1))
    print(result.rstrip())