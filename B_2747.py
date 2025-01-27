N = int(input())

F = []
seq = 0
F.append(seq)
seq += 1
F.append(seq)

for i in range(N):
    seq = F[i] + F[i + 1]
    F.append(seq)

print(F[N])


