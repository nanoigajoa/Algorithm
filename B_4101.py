list = []

while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break
    
    if b >= a:
        list.append("No")
    else:
        list.append("Yes")

for i in list:
    print(i)