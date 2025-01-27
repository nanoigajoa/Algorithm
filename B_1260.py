from collections import deque, defaultdict

def dfs(graph, start_node):
    visited = []
    stack = [start_node]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(sorted(graph[node], reverse=True))
    return visited

def bfs(graph, start_node):
    visited = []
    queue = deque([start_node])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(sorted(graph[node]))  # 큐에서는 순차적으로 처리(FIFO)하므로 정렬된 순서대로 추가
    return visited

import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = defaultdict(list)

# 간선 정보 입력받기
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(' '.join(map(str, dfs(graph, V))))
print(' '.join(map(str, bfs(graph, V))))
