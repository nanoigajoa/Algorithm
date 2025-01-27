S = str(input().upper())
# print(S, ':S')
S1 = list(set(S))
# print(S1, ':S1')

cnt = []

for i in S1:
    count = S.count(i)
    cnt.append(count)
    # print(count, ':count')

# print(cnt, ':cnt')

if cnt.count(max(cnt)) > 1:
  print("?")

else:
  print(S1[cnt.index(max(cnt))])