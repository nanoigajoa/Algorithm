import sys
input = sys.stdin.readline

stack_1 = list(input().rstrip())
stack_2 = []

for i in range(int(input())):
    cmd = list(input().split())

    if cmd[0] == 'L':
        if stack_1:
            stack_2.append(stack_1.pop())
    
    elif cmd[0] == 'D':
        if stack_2:
            stack_1.append(stack_2.pop())

    elif cmd[0] == 'B':
        if stack_1:
            stack_1.pop()

    else:
        stack_1.append(cmd[-1])

stack_1.extend(reversed(stack_2))
print(''.join(stack_1))