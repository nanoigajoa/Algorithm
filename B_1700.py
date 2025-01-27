import sys
input = sys.stdin.readline

N, K = map(int, input().split())
use = list(map(int, input().split()))
visited = []
count = 0

for i in range(K):
    if use[i] in visited:
        continue
    
    if len(visited) < N:
        visited.append(use[i])
    else:
        # 멀티탭에 꽂힌 기기 중 가장 나중에 사용되거나, 더 이상 사용되지 않는 기기를 찾음
        farthest = -1
        remove_device = None

        for device in visited:
            if device not in use[i+1:]:
                remove_device = device
                break
            else:
                next_use = use[i+1:].index(device)
                if next_use > farthest:
                    farthest = next_use
                    remove_device = device

        # 교체
        visited.remove(remove_device)
        visited.append(use[i])
        count += 1

print(count)
