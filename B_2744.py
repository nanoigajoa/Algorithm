s = list(str(input()))

for i in range(len(s)):
    if 'a' <= s[i] <= 'z': 
        s[i] = chr(ord(s[i]) - 32)
    elif 'A' <= s[i] <= 'Z':
        s[i] = chr(ord(s[i]) + 32)

print(''.join(s))

