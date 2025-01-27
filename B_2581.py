M = int(input())
N = int(input())

num_L = []

for num in range(M, N + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            num_L.append(num)

if num_L:
    print(sum(num_L))
    print(min(num_L))
else:
    print(-1)