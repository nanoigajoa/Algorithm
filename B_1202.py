import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
m_v = [tuple(map(int, input().split())) for _ in range(N)]
m_v.sort(key=lambda x:(x[0], -x[1]))

bag_mass = [int(input()) for _ in range(K)]
bag_mass.sort()

heap = []
value = 0
j = 0

for i in range(K):
    while j < N and bag_mass[i] >= m_v[j][0]:
        heapq.heappush(heap, -m_v[j][1])  # 최대 힙을 만들기 위해 음수로 저장합니다.
        j += 1
    if heap:
        value += heapq.heappop(heap)  # 최대 힙에서 가장 큰 값을 꺼내서 value에 추가합니다.

print(-value)
