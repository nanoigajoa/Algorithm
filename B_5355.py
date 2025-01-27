T = int(input())

for i in range(T):
    testcase = input().split()

    answer = float(testcase[0])

    for op in testcase[1:]:
        if op == '@':
            answer *= 3
        elif op == '#':
            answer -= 7
        elif op == '%':
            answer += 5
    
    print(f'{answer:.2f}')
