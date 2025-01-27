import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = deque([1+i for i in range(N)])

for i in range(N-1):
    q.popleft()
    cur = q[0]
    q.remove(cur)
    q.append(cur)
    # print(q)

print(*q)