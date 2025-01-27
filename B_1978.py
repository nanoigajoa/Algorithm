N = int(input())

S = list(map(int, input().split()))
final = []

for i in range(len(S)):
    if S[i] < 2:
        continue
    
    a = 2
    is_prime = True

    while a * a <= S[i]:
        if S[i] % a == 0:
            is_prime = False
            break
        a += 1
    
    if is_prime:
        final.append(S[i])

print(len(final))















