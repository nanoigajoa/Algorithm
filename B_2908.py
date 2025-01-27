A, B = map(str, input().split())

re_A = A[::-1]
re_B = B[::-1]

if int(re_A) > int(re_B):
    print(re_A)
elif int(re_A) < int(re_B):
    print(re_B)
else:
    pass