import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
num.sort()  # 오름차순 정렬
count = 0

for i in range(N):
    target = num[i]
    start, end = 0, N - 1
    
    while start < end:
        current_sum = num[start] + num[end]
        
        # 자기 자신은 사용 X
        if start == i:
            start += 1
            continue
        if end == i:
            end -= 1
            continue
        
        if current_sum == target:
            count += 1
            break
        elif current_sum < target:
            start += 1
        else:
            end -= 1

print(count)
