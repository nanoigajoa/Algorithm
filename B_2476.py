people = int(input())

prizel = []

for i in range(people):
    a, b, c = map(int, input().split())
    if a == b == c:
        prize = 10000 + a * 1000
    elif a == b or a == c:
        prize = 1000 + a * 100
    elif b == c:
        prize = 1000 + b * 100
    elif a != b != c:
        prize = max(a, b, c) * 100

    prizel.append(prize)

print(max(prizel))