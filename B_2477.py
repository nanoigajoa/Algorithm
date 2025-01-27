import sys
input = sys.stdin.readline

K = int(input())

sides = []
hor = []
ver = []

for _ in range(6):
    dir, len = map(int, input().split())
    sides.append((dir, len))

    if dir == 1 or dir == 2:
        hor.append((dir, len))
    if dir == 3 or dir == 4:
        ver.append((dir, len))

if hor:
    max_hor_side = max(hor, key=lambda x: x[1])
    max_hor_side_idx = sides.index(max_hor_side)

if ver:
    max_ver_side = max(ver, key=lambda x: x[1])
    max_ver_side_idx = sides.index(max_ver_side)

left_hor_idx = (max_hor_side_idx - 1) % 6
right_hor_idx = (max_hor_side_idx + 1) % 6

left_ver_idx = (max_ver_side_idx - 1) % 6
right_ver_idx = (max_ver_side_idx + 1) % 6

max_hor_length = sides[max_hor_side_idx][1]
max_ver_length = sides[max_ver_side_idx][1]

left_hor_length = sides[left_hor_idx][1]
right_hor_length = sides[right_hor_idx][1]

left_ver_length = sides[left_ver_idx][1]
right_ver_length = sides[right_ver_idx][1]

area = max_hor_length * max_ver_length - (abs(left_hor_length - right_hor_length) * abs(left_ver_length - right_ver_length))

print(K * area)