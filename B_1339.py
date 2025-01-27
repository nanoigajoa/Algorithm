import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]

weight = defaultdict(int)

for word in words:
    length = len(word)
    for idx, char in enumerate(word):
        weight[char] += 10 ** (length - idx - 1)

sorted_weights = sorted(weight.items(), key=lambda x: x[1], reverse=True)

num = 9  # 가장 큰 숫자부터 할당
char_to_num = {}
for char, _ in sorted_weights:
    char_to_num[char] = num
    num -= 1  # 다음 숫자

total_sum = 0
for word in words:
    number = int(''.join(str(char_to_num[char]) for char in word))
    total_sum += number

print(total_sum)
