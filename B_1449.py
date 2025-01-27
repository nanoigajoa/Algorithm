import sys
input = sys.stdin.readline

N, L = map(int, input().split())  # N: 누수 지점의 수, L: 테이프의 길이
leak = list(map(int, input().split()))
leak.sort()  # 누수 지점을 오름차순 정렬

L_count = 0  # 사용한 테이프의 수
i = 0  # 누수 지점의 인덱스

while i < N:
    # 현재 지점에서 테이프를 붙이고, 이 테이프가 커버할 수 있는 마지막 지점을 계산
    L_count += 1  # 테이프 사용
    end = leak[i] + L - 1  # 현재 테이프가 커버하는 마지막 위치
    
    # 테이프가 커버하는 범위 안에 있는 누수 지점들을 모두 건너뜀
    while i < N and leak[i] <= end:
        i += 1

print(L_count)  # 최소 사용한 테이프 수 출력
