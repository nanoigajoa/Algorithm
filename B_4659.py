import sys
input = sys.stdin.readline

vowels = ['a','e','i','o','u']

while True:
    score = 0
    vowel_count = 0
    consonant_count = 0

    T = str(input().strip())
    if T == 'end':
        break

    for i in T:     #모음확인
        if i in vowels:
            score += 1
            break
            
    valid = True
    for j in range(len(T) - 1):
        if T[j] == T[j + 1] and T[j] not in ['e', 'o']:
            valid = False
            break
    if valid == True:
        score += 1

    valid2 = True
    for k in T:                     # 모음3개 자음3개 연속x
        if k in vowels:
            vowel_count += 1
            consonant_count = 0
            if vowel_count < 3:
                continue
            else:
                valid2 = False
                break
        else:
            consonant_count += 1
            vowel_count = 0 
            if consonant_count < 3:
                continue
            else:
                valid2 = False
                break
    if valid2 == True:
        score += 1

    if score == 3:
        print(f'<{T}> is acceptable.')
    else:
        print(f'<{T}> is not acceptable.')