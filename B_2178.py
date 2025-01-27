import sys
input = sys.stdin.readline

def bfs(si, sj):
    q = []
    q.append((si, sj, 1))
    v[si][sj] = 1

    while q:
        ci, cj, dist = q.pop(0)

        if ci == N - 1 and cj == M - 1:
            return dist

        for di, dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append((ni, nj, dist + 1))
                v[ni][nj] = 1
    return -1

N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
# print(arr)
v = [[0] * M for _ in range(N)]
# print(v)

print(bfs(0, 0))