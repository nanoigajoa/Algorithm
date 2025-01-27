import re

S = input()
result = re.findall(r'\d+|[+\-*/]', S)

result = [num.lstrip('0') if num.isdigit() else num for num in result]
result = ['0' if num == '' else num for num in result]

if len(result) > 3:
    for i in range(1, (len(result) - 1) // 2 + 1):
        if result[2*i - 1] == '-':
            new_S = result[2*i::2]
            prev_S = result[2*i - 2::-2]
            break

    if '-' not in result:
        none_S = ''.join(result)
        print(eval(none_S))
    
    else:
        new_S1 = sum(int(num) for num in new_S)
        prev_S1 = sum(int(num) for num in prev_S)
        print(prev_S1 - new_S1)

else:
    none_S = ''.join(result)
    print(eval(none_S))