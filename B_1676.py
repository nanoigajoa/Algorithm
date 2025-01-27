N = int(input())
num = N
for i in range(1, N - 1):
    num *= N - i
    
result = str(num)
rresult = list(result[::-1])
count = 0

for j in range(len(rresult) - 1):
    if rresult[j] == '0' and rresult[j+1] == '0':
        count += 1
    elif rresult[j] == '0' and rresult[j+1] != '0':
        count += 1
        break

print(count)