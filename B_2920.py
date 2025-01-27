i = list(map(int, input().split()))

if i == sorted(i):
    print('ascending')
elif i == sorted(i, reverse=True):
    print('descending')
else:
    print('mixed')