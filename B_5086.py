A = []
B = []

while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break
    A.append(a)
    B.append(b)

for a, b in zip(A, B):
    if b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')
