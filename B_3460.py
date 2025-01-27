T = int(input())
indices = []

for i in range(T):
    N = int(input())
    result = bin(N)[2:]
    Result = result[::-1]
    # print(Result)
    A = list(Result)

    for index, char in enumerate(A):
        if char == '1':
            indices.append(index)

    print(' '.join(map(str, indices)))
    indices = []

