# import sys
# input = sys.stdin.readline

# ex = ['IO', 'I']

# N = int(input())
# M = int(input())
# S = input()
# current = N*ex[0] + ex[1]
# count = 0
# # print(current)

# for i in range(M-2):
#     if S[i:N*2+i+1:] == current:
#         count += 1

# print(count)

import sys
input = sys.stdin.readline

N = int(input())  # 'IOI'가 반복되는 횟수
M = int(input())  # 문자열 S의 길이
S = input().strip()  # 문자열 입력

count = 0  # N번 반복된 패턴의 개수를 셀 변수
pattern_count = 0  # IOI 패턴이 몇 번 연결되었는지 추적
i = 0  # 문자열 탐색을 위한 인덱스

while i < M - 1:
    # 'IOI' 패턴이 시작되는 부분을 확인
    if S[i:i+3] == 'IOI':
        pattern_count += 1
        i += 2  # 'IOI' 패턴을 찾았으므로 두 칸 건너뜀

        # N번 반복되는 패턴을 찾으면 카운트를 증가
        if pattern_count == N:
            count += 1
            pattern_count -= 1  # 패턴을 찾았으므로 'I'만큼 다시 빼기
    else:
        # 패턴이 끊기면 패턴 카운트를 초기화
        pattern_count = 0
        i += 1  # 다음 문자로 이동

print(count)
