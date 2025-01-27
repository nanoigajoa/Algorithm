N, M = map(int, input().split())

Package = []
each = []
for _ in range(M):
    A, B = map(int, input().split())
    Package.append(A)
    each.append(B)

Package.sort()
each.sort()
# print(Package)
# print(each)

count = 0
result = 0
index_P = 0
index_e = 0

while count < N:

    if N < 6:
        if Package[index_P] < each[index_e] * N:
            result += Package[index_P]
            count += 6
        else:
            result += each[index_e] * N
            count += N

    elif N >= 6:
        if N - count >= 6:
            if Package[index_P] < each[index_e] * 6:
                result += Package[index_P]
                count += 6
            else:
                result += each[index_e] * 6
                count += 6
        else:
            remaining = N - count
            if Package[index_P] < each[index_e] * remaining:
                result += Package[index_P]
                count += 6
            else:
                result += each[index_e] * remaining
                count += remaining

print(result)