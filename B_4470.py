import sys
input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]

for i in range(len(words)):
    print(f"{i+1}. {words[i]}")