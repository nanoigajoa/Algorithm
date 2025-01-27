import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    count = 1  # 첫 번째 사람은 무조건 카운트
    grade_L = []
    N = int(input())
    
    for _ in range(N):
        grade = list(map(int, input().split()))
        grade_L.append(grade)

    # 첫 번째 점수를 기준으로 오름차순 정렬
    grade_L.sort(key=lambda x: x[0])
    
    min_second = grade_L[0][1]
    
    for i in range(1, N):
        if grade_L[i][1] < min_second:
            count += 1
            min_second = grade_L[i][1]

    print(count)
