T = int(input())

for i in range(T):
    result = []
    num = list(map(int, input().split()))
    
    for j in num:
        if j % 2 == 0:
            result.append(j)
        else:
            pass
    result.sort()
    print(sum(result), result[0])