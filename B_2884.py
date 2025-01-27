H, M = map(int, input().split())

if M < 45:
    H -= 1
    M += 15
    if H < 0:
        H += 24

elif M == 45:
    M -= 45

elif M > 45:
    M -= 45
    if H > 24:
        H -= 24

print(H, M)
