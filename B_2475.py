N = list(map(int, input().split()))
a = 0

for num in N:
    a += num ** 2

result = a % 10

print(result)