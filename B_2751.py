import sys
input = sys.stdin.readline

N = int(input())
a = [int(input()) for i in range(N)]
a.sort()

for i in a:
    print(i)