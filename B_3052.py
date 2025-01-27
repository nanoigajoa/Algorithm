import sys
N = sys.stdin.readline

a = set()

for i in range(10):
    N = int(input())

    result = N % 42
    a.add(result)

print(len(a))