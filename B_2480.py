a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif a == b and b != c:
    print(1000 + b * 100)
elif a == c and b != c:
    print(1000 + a * 100)
elif b == c and a != c:
    print(1000 + b * 100)
elif a != b != c:
    prize = max(a, b, c) * 100
    print(prize)