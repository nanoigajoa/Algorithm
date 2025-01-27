n = int(input())

for i in range(n):
    space_1 = ' ' * i
    star = '*' * (2 * (n - i) - 1)
    result = space_1 + star + space_1
    print(result.rstrip())
    
for i in range(n - 2, -1, -1):
    space_1 = ' ' * i
    star = '*' * (2 * (n - i) - 1)
    result = space_1 + star + space_1
    print(result.rstrip())