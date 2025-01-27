import sys
input = sys.stdin.readline

T = int(input().strip())
results = []

for _ in range(T):
    N, Q = map(int, input().split())
    importance = list(map(int, input().split()))

    # 큐 초기화 (인덱스와 중요도를 함께 저장)
    queue = [(i, importance[i]) for i in range(N)]
    print_order = 0

    while queue:
        current = queue.pop(0)  # 큐의 맨 앞 요소를 꺼냄
        if any(current[1] < item[1] for item in queue):
            # 현재 문서보다 중요도가 높은 문서가 있으면 다시 큐에 넣음
            queue.append(current)
        else:
            # 현재 문서의 중요도가 가장 높음
            print_order += 1
            if current[0] == Q:
                results.append(print_order)
                break

# 결과 출력
for result in results:
    print(result)
