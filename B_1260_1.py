import sys
input = sys.stdin.readline

def dfs(c):
    ans_dfs.append(c) #단위실행
    v_d[c] = 1

    for n in adj[c]:
        if v_d[n] == 0:  #방문하지 않았다면
            dfs(n) #재귀로 방문처리

def bfs(s):
    q = []
    q.append(s)
    ans_bfs.append(s)
    v_b[s] = 1

    while q:
        c = q.pop(0)
        for i in adj[c]:
            if v_b[i] == 0:
                q.append(i)
                ans_bfs.append(i)
                v_b[i] = 1

N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

for i in range(1, N+1):
    adj[i].sort()

v_d = [0] * (N+1)
ans_dfs = []
dfs(V)

v_b = [0] * (N+1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)