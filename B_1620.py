import sys
input = sys.stdin.readline

N, M = map(int, input().split())
inventory = [input().strip() for i in range(N)]
name_to_index = {name: idx + 1 for idx, name in enumerate(inventory)}

for _ in range(M):
    answer = input().strip()

    if answer.isdigit():
        index = int(answer) - 1
        print(inventory[index])

    else:
        print(name_to_index[answer])