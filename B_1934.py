import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

T = int(input())
test_cases = []

for _ in range(T):
    A, B = map(int, input().split())
    test_cases.append((A, B))

for A, B in test_cases:
    print(lcm(A, B))