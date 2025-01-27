T = int(input())

for i in range(T):
    N = int(input())
    result = []
    
    store = list(map(int, input().split()))
    store.sort(reverse=True)

    for j in range(N-1):
        num = 0
        num = store[j] - store[j + 1]
        result.append(num)

    print(sum(result) * 2)
