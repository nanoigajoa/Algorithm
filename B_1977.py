M = int(input())
N = int(input())

final = []

for i in range(M, N + 1):
    if (i ** 0.5).is_integer():
        final.append(i)

if final:
    print(sum(final))
    print(min(final))
else:
    print(-1)
