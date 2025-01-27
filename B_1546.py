N = int(input())

grade = list(map(int, input().split()))
M = max(grade)

New = []

for i in grade:
    new = i / M * 100
    New.append(new)

result = sum(New) / len(New)
print(result)
