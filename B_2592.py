num_L = []
result_L = []

for i in range(10):
    num = int(input())
    num_L.append(num)

for j in num_L:
    result = num_L.count(int(j))
    result_L.append((result, j))

final = sorted(result_L, reverse=True)
print(int(sum(num_L) / 10))
print(final[0][1])