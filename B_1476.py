E, S, M = map(int, input().split())

e, s, m = 1, 1, 1
count = 1

while True:
    if e == E and s == S and m == M:
        print(count)
        break
    
    e = e % 15 + 1
    s = s % 28 + 1
    m = m % 19 + 1
    
    count += 1


# 이해 안됨
# E, S, M = map(int, input().split())

# year = 1

# while True:
#     if (year - E) % 15 == 0 and (year - S) % 28 == 0 and (year - M) % 19 == 0:
#         print(year)
#         break
#     year += 1