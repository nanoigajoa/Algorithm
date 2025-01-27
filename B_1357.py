X, Y = map(str, input().split())

a = str(int(X[::-1]) + int(Y[::-1]))

print(a[::-1].lstrip('0'))
