import sys
input = sys.stdin.readline

board = [list(input().rstrip()) for i in range(8)]
white = 0

for i in range(len(board)):
    for j in range(len(board[i])):
        if i % 2 == 0 and j % 2 == 0: #i가 짝수이면서 j도 짝수
            if board[i][j] == "F":
                white += 1
        elif i % 2 != 0 and j % 2 != 0:  #i가 홀수이면서 j도 홀수
            if board[i][j] == "F":
                white += 1
print(white)