import sys
input = sys.stdin.readline

N = int(input().strip())

table = [list(map(int, input().strip().split())) for _ in range(N)]

table.sort(key=lambda x: (x[1], x[0]))

result = [table[0]]

for j in range(1, len(table)):
    if table[j][0] >= result[-1][1]:
        result.append(table[j])

print(len(result))