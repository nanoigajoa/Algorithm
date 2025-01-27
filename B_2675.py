T = int(input())

test = []

for i in range(T):
    R, S = input().split()
    R = int(R)
    P = ''.join([char * R for char in S])
    test.append(P)
print('\n'.join(test))