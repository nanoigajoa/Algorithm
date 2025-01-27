N = int(input())

NL = []

for i in range(N):
    num = int(input())
    NL.append(num)

result = sorted(NL)

for j in range(N):
    print(result[j])