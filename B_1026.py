import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(enumerate(map(int, input().split())))
A.sort() # 오름차순
B.sort(key=lambda x : -x[1]) # 내림차순
result = []

# B를(인덱스, 요소)로 바꾸고, 오름차순, 내림차순 해서 원래 인덱스 자리로 반환

for i in range(N):
    res = (A[i] * B[i][1], B[i][0])
    result.append(res)

final = [j[0] for j in result]
print(sum(final))