# S = int(input())
# natural = 0
# natural_list = []
# result = sum(natural_list)

# while S >= result:
#     if result <= S:
#         natural += 1
#         natural_list.append(natural)
#         result = sum(natural_list)
# print(len(natural_list) - 1)

S = int(input())
natural = 0
result = 0

while result <= S:
    natural += 1
    result += natural

print(natural - 1)
