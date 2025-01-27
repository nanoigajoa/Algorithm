S = input().strip(' ')
count = 1

if not S:
    count = 0
else:
    for i in range(len(S)):
        if S[i] == ' ':
            count += 1

print(count)