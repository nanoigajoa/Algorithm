import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

for i in range(1, N+1):
    if i > 99:
        if (i // 100) - ((i - 100*(i // 100)) // 10) == ((i - 100*(i // 100)) // 10) - (i % 10):
            # 321일 경우 3 - (321 - 300) - 2 - *(321 - 300 - 
            cnt += 1
    else:
        cnt += 1

print(cnt)