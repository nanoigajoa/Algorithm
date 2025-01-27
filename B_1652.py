N = int(input())

bed_x = 0
bed_y = 0

data = []

for i in range(N):
    sit = input().strip()
    data.append(sit)

for row in data:
    parts = row.split('X')
    for part in parts: # 이 부분이 이해가 안감
        if len(part) >= 2:
            bed_x += 1

for col in range(N):
    vertical = ''
    for row in range(N):
        vertical += data[row][col]
    parts = vertical.split('X')
    for part in parts:
        if len(part) >= 2:
            bed_y += 1

print(bed_x, bed_y)
