i = input()
stack = []
atom = {'H':1, 'C':12, 'O':16}

for i in i:
    if i == '(':
        stack.append(i)
    
    elif i == 'H' or i == 'C' or i == 'O':
        stack.append(atom[i])
    
    elif i == ')':
        num = 0
        while True:
            if stack[-1] == '(':
                stack.pop()
                stack.append(num)
                break
            else:
                num += stack.pop()
    else:
        stack.append(stack.pop()*int(i))

print(sum(stack))