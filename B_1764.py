import sys
input = sys.stdin.readline

N, M = map(int, input().split())

hear = []
see = []

for _ in range(N):
    hear.append(input().rstrip())

for _ in range(M):
    see.append(input().rstrip())

result = list(set(hear) & set(see))
result.sort()

print(len(result))

for i in result:
    print(i)