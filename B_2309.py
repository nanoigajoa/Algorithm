from itertools import combinations

seven = 0
key_list = []

for i in range(9):
    key = int(input())
    key_list.append(key)

for j in combinations(key_list, 7):
    if sum(j) == 100:
        result = sorted(j)
        for k in result:
            print(k)
        break