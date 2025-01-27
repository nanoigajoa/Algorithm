import sys
input = sys.stdin.readline

N = int(input())
result = []
temp = []

for i in range(N):
    S = str(input())
    for j in S:
        if j.isdigit():
            temp.append(j)
        else:
            if temp:
                result.append(int(''.join(temp)))
                temp = []
result.sort()

for k in result:
    print(k)
            


