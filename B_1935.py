N = int(input())
calcul = list(input())
stack = []
result = []
alphabet = {}  # 알파벳과 숫자의 매핑을 저장할 딕셔너리

for cal in calcul:
    if 'A' <= cal <= 'Z':
        if cal not in alphabet:  # 딕셔너리에 해당 알파벳이 없으면 숫자 입력 받기
            number = int(input())
            alphabet[cal] = number  # 딕셔너리에 저장
        result.append(alphabet[cal])  # 딕셔너리에서 숫자를 가져와 추가
    else:
        result.append(cal)

for i in result:
    if isinstance(i, int):
        stack.append(i)
    else:
        b = stack.pop()
        a = stack.pop()
        if i == '+':
            stack.append(a + b)
        elif i == '-':
            stack.append(a - b)
        elif i == '*':
            stack.append(a * b)            
        elif i == '/':
            stack.append(a / b)
print(f'{stack[-1]:.2f}')