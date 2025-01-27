import heapq
import sys
input = sys.stdin.readline

heap = []
final = []

N = int(input())

for i in range(N):
    value = int(input())

    if value == 0 and heap:
        result = heapq.heappop(heap)
        final.append(result)
    elif value == 0:
        final.append(0)
    elif value != 0:
        heapq.heappush(heap, value)

for f in final:
    print(f)
