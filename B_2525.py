A, B = map(int, input().split())  # 입력으로 시간 A와 분 B을 받습니다.
C = int(input())  # 추가적인 분을 입력 받습니다.

# 시간과 분을 계산합니다.
total_minutes = A * 60 + B + C
hour, minute = divmod(total_minutes, 60)

if hour >= 24:
    print(hour - 24, minute)
else:
    print(hour, minute)
