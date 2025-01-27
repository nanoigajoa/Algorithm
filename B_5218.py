T = int(input())
for i in range(T):
    S = input().split()

    D = []

    for j in range(len(S[0])):
        if ord(S[1][j]) - ord(S[0][j]) < 0:
            d = 26 - (ord(S[0][j]) - ord(S[1][j]))
            D.append(d)
        else:
            d = ord(S[1][j]) - ord(S[0][j])
            D.append(d)

    print(f'Distances:', *D)
