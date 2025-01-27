X = []
Y = []

for i in range(3):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

x = next(p for p in X if X.count(p) == 1)
y = next(p for p in Y if Y.count(p) == 1)

print(x, y)
