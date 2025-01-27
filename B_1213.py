name = list(input())
middle = []
half = []

# 1. 각 문자의 개수 세기
result = [(i, name.count(i)) for i in name]

# 2. 중복 제거
result = list(set(result))

# 3. 문자를 기준으로 정렬
result.sort(key=lambda x: x[0])
# print(result, 'result')
# print(len(name), 'len(name)')

if len(name) % 2 == 0:  # 문자개수 짝수일 때
    palindrome = []
    for char, count in result:
        if count % 2 == 0:
            half.extend([char] * (count // 2))
        else:
            palindrome = []
            break
    else:
        palindrome = half + half[::-1]

else: # 문자개수 홀수일 때
    odd_count = 0
    for char, count in result:
        if count % 2 != 0:
            if odd_count == 0:
                middle = char
                odd_count += 1
            else:
                palindrome = []
                break
        half.extend([char] * (count // 2))
    else:
        palindrome = half + [middle] + half[::-1]

if palindrome:
    print(''.join(palindrome))
else:
    print('I\'m Sorry Hansoo')