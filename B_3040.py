import random
import sys
N = sys.stdin.readline

age = []

for i in range(9):
    N = int(input())
    age.append(N)

while True:
    random.shuffle(age)
    select_age = age[:7]

    if sum(select_age) == 100:
        for i in select_age:
            print(i)
        break