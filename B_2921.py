N = int(input())
result_L = []

for i in range(N + 1):
    for j in range(i, N + 1):
        result_L.append((i, j))

print(sum(sum(t) for t in result_L))