n = int(input())

fibonach = [0, 1]

for i in range(n):
    next = fibonach[i] + fibonach [i + 1]
    fibonach.append(next)
    fibonach.sort()

print(fibonach[n])