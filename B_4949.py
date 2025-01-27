import sys
input = sys.stdin.readline

s_list = []

while True:
    s = input().rstrip()  # 입력받은 문자열의 양 끝 공백 제거 (특히 줄바꿈 문자)

    if s[0] == '.':  # 입력이 '.'이면 종료
        break

    s_nospace = s.replace(' ', '')
    s_list.append(s_nospace)

for i in s_list:
    stack = []
    for j in range(len(i)):
        if i[j] in ('(', '['):
            stack.append(i[j])

        elif i[j] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i[j])

        elif i[j] == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i[j])

        else:
            continue

    if stack:
        print('no')
    else:
        print('yes')
