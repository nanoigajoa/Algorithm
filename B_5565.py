total = int(input())

total_L = []

for i in range(9):
    resp = int(input())
    total_L.append(resp)

print(total - sum(total_L))