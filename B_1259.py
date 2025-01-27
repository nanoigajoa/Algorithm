import sys
input = sys.stdin.readline

while True:
    S = input().strip()

    if S == 0 or S == "0":
        break
    else:
        if S == S[::-1]:
            print("yes")
        else:
            print("no")

