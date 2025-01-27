# import sys
# input = sys.stdin.readline

# N = int(input())
# count = 0

# for _ in range(N):
#     char_L = []
#     TF = True
#     result = True

#     S = input().rstrip()

#     for char in S:

#         if char_L and char != char_L[-1]: # 다른 알파벳으로 넘어갔을 경우
#             TF = False
#         if char_L and char == char_L[-1]: # 같은 알파벳일 경우
#             TF = True

#         if not char_L: # 첫번째
#             char_L.append(char)

#         if TF == False and char in char_L:
#             count += 1
#             break

#         elif TF == False and char not in char_L:
#             char_L.append(char)

# print(N - count)

import sys
input = sys.stdin.readline

n = int(input())
cnt = n

for _ in range(n) :
    word = input()
    for i in range(len(word)-1) :
        if word[i] == word[i+1] :
            pass
        elif word[i] in word[i+1:] :
            cnt -= 1
            break

print(cnt)