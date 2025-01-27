import sys
input = sys.stdin.readline

def dfs(x):
    result.append(x) #단위실행
    v[x] = 1

    for n in adj[x]:
        if v[n] == 0: #방문하지 않았다면
            dfs(n) #재귀로 방문처리

Computer_num = int(input())
edge = int(input())
adj = [[] for _ in range(Computer_num + 1)]

for _ in range(edge):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

v = [0]*(Computer_num + 1) #방문처리 리스트
result = []
dfs(1)

print(len(result)-1)