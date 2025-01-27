import sys
N = sys.stdin.readline

score_L = []
idx = []
a = 0

for i in range(8):
    N = int(input())
    score_L.append((N, i + 1))
    score_L.sort(reverse=True)
    score = score_L[:5]

for j in range(len(score)):
    a += score[j][0]
    idx.append(str(score[j][1]))
idx.sort()

print(a)
print(*idx)