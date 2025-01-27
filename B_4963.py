import sys
input = sys.stdin.readline

def bfs(si, sj):
    q = []
    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<h and 0<=nj<w and v[ni][nj] == 0 and Map[ni][nj] == 1:
                q.append((ni,nj))
                v[ni][nj] = 1

while True:
    result = []
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    cnt = 0
    Map = [list(map(int, input().split())) for _ in range(h)]
    v = [[0] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if Map[i][j] == 1 and v[i][j] == 0:
                bfs(i, j)
                cnt += 1
    print(cnt)