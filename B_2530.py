A, B, C = map(int, input().split()) 
D = int(input())

total_second = A * 3600 + B * 60 + C + D
hour, remainder = divmod(total_second, 3600)
minute, second = divmod(remainder, 60)

if hour >= 24:
    hour %= 24

print(hour, minute, second)