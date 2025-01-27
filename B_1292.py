A, B = map(int, input().split())

L = []

for i in range(46):
    for j in range(i):
        L.append(i)

# print(len(L))
# print(L[A - 1 : B + 1])
print(sum(L[A-1:B]))