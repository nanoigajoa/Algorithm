A = int(input())
B = int(input())
C = int(input())

pro = A * B * C
dup = list(str(pro))

for i in range(10):
    result = dup.count(str(i))
    print(result)

# A = int(input())
# B = int(input())
# C = int(input())

# # A, B, C의 곱을 계산한 후 리스트로 변환합니다.
# product = A * B * C
# dup = list(str(product))  # A * B * C의 각 자리 숫자를 리스트의 요소로 만듭니다.

# # 0부터 9까지의 숫자가 몇 번 등장하는지를 카운트합니다.
# for i in range(10):
#     result = dup.count(str(i))  # 문자열로 변환하여 해당 숫자의 등장 횟수를 세어 저장합니다.
#     print(result)
