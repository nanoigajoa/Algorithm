n = int(input())

for i in range(n):
    stars = '*' * (i + 1)
    spaces = ' ' * (2 * (n - i - 1))
    print(stars + spaces + stars)
    
for i in range(n - 2, -1, -1):
    stars = '*' * (i + 1)
    spaces = ' ' * (2 * (n - i - 1))
    print(stars + spaces + stars)