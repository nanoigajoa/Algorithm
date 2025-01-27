# curent = 0

# compare = []

# for i in range(10):
#     o, i = map(int, input().split())

#     curent -= o
#     curent += i

#     compare.append(curent)

# result = sorted(compare, reverse=True)

# print(result[0])

import sys
data = [sys.stdin.readline().strip() for i in range(10)]

current = 0
compare = []

for line in data:
    o, i = map(int, line.split())
    current -= o
    current += i
    compare.append(current)

result = max(compare)
print(result)