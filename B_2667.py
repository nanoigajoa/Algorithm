import sys
input = sys.stdin.readline

def bfs(si,sj):
    q = []
    q.append((si,sj))  #큐 초기데이터 삽입하고 방문표시
    v[si][sj] = 1
    cnt = 1

    while q:
        ci,cj = q.pop(0)
        for di, dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append((ni, nj))
                v[ni][nj] = 1
                cnt += 1
    return cnt

N = int(input())
arr = [list(map(int, input().strip())) for _ in range(N)]
v = [[0]*N for _ in range(N)]   # 1=방문, 0=미방문
result = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and v[i][j] == 0:  #방문하지 않은 집 발견시 bfs 실행
            result.append(bfs(i,j))

result.sort()
print(len(result), *result, sep='\n')
