B_L = []
for i in range(3):
    B = int(input())
    B_L.append(B)
    B_L.sort()

J_L = []
for j in range(2):
    J = int(input())
    J_L.append(J)
    J_L.sort()

print(B_L[0] + J_L[0] - 50)