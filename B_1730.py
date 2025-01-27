# 배열 탐색

N = int(input())
move = input()

grid = [['.'] * N for _ in range(N)]
x, y = 0, 0

def update_grid(x, y, direction):
    if grid[x][y] == '.':
        grid[x][y] = '|' if direction in 'UD' else '-'
    elif (grid[x][y] == '|' and direction in 'LR') or (grid[x][y] == '-' and direction in 'UD'):
        grid[x][y] = '+'

for direction in move:
    next_x, next_y = x, y
    
    if direction == 'D':
        next_x += 1
    elif direction == 'U':
        next_x -= 1
    elif direction == 'R':
        next_y += 1
    elif direction == 'L':
        next_y -= 1
    
    if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N:
        continue
    
    if next_x != x:
        step = 1 if next_x > x else -1
        for i in range(x, next_x + step, step):
            update_grid(i, y, direction)
    elif next_y != y:
        step = 1 if next_y > y else -1
        for j in range(y, next_y + step, step):
            update_grid(x, j, direction)
    
    x, y = next_x, next_y

for row in grid:
    print(''.join(row))