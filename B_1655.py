import sys
import heapq
input = sys.stdin.readline

N = int(input())
left_heap = []  # 최대 힙 (중간 값보다 작은 값들)
right_heap = []  # 최소 힙 (중간 값보다 큰 값들)
result = []

for _ in range(N):
    num = int(input())

    # 최대 힙에 삽입 (최대 힙은 음수 값을 사용하여 구현)
    if len(left_heap) == 0 or num <= -left_heap[0]:
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)

    # 균형 맞추기
    if len(left_heap) > len(right_heap) + 1:
        heapq.heappush(right_heap, -heapq.heappop(left_heap))
    elif len(right_heap) > len(left_heap):
        heapq.heappush(left_heap, -heapq.heappop(right_heap))

    # 중간 값 추가
    result.append(-left_heap[0])

for j in result:
    print(j)
