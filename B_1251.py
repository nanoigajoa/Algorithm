S = list(input())
sorted = sorted(S)
# print(S)
div = []

for i in range(2):
    div.append(sorted[i])

list = []

for j in S:
    if j in div:
        list.append(j)
        list.append(" ")
    else:
        list.append(j)

result = ''.join(list).split(" ")
# print(result)
reversed = [k[::-1] for k in result]
print(''.join(reversed))