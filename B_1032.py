import sys
input = sys.stdin.readline

N = int(input())
current = 0
files = [list(input().rstrip()) for _ in range(N)]

for i in range(len(files[0])):
    for j in range(N):
        if j == 0 or current == files[j][i]:
            if files[j-1][i] == '?':
                files[j][i] = '?'
            current = files[j][i]
        
        else:
            if files[j-1][i] == '?':
                files[j][i] = '?'
            files[j][i] = '?'

    current = 0

print("".join(files[-1]))