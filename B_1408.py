C_time = input().split(':')
S_time = input().split(':')

final = []
final.append(C_time)
final.append(S_time)

for i in range(2):
    for j in range(3):
        final[i][j] = int(final[i][j])

if final[1][0] < final[0][0]:
    final[1][0] += 24

for i in range(2, 0, -1):
    if final[1][i] < final[0][i]:
        final[1][i] += 60
        final[1][i-1] -= 1

result = [
    final[1][0] - final[0][0],
    final[1][1] - final[0][1],
    final[1][2] - final[0][2]
]

print(f"{result[0]:02d}:{result[1]:02d}:{result[2]:02d}")