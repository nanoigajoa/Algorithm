import sys
input = sys.stdin.readline

N = int(input())
S = set(map(int, input().split()))

M = int(input())
confirm_num = list(map(int, input().split()))

for i in range(len(confirm_num)):
    if confirm_num[i] in S:
        print(1)
    else:
        print(0)