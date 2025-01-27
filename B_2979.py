A, B, C = map(int, input().split())

Time = [0] * 100
price = 0

for i in range(3):
    arr, dep = map(int, input().split())
    for j in range(arr, dep):
        Time[j] += 1

for k in Time:
    if k == 1:
        price += A
    elif k == 2:
        price += (B * 2)
    elif k == 3:
        price += (C * 3)

print(price)