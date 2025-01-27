N = int(input().strip())

original = N
cycle = 0

while True:
    if original == N and cycle != 0:
        break

    if N < 10:
        N = N * 11 
    else: # 26를 문자열 인덱스를 사용하지 않고 2와 6을 구하는 방법(10의자리, 1의자리 구하기)
        tens = N // 10
        ones = N % 10
        N = ones * 10 + (tens + ones) % 10

    cycle += 1

print(cycle)