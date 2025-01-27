board = list(input().split('.'))
result = []
card = ['AAAA', 'BB']
TF = True

for part in board:
    L = len(part)

    if L % 2 != 0:
        print(-1)
        TF = False
        break

    while L >= 4:  # 4로 나눌 수 있는 만큼 'AAAA'를 채워 넣음
        result.append(card[0])
        L -= 4

    if L == 2:
        result.append(card[1])

    result.append('.')  # 각 부분 사이에 '.'을 다시 붙여줌

if result:
    result.pop()

if TF == True:
    print(''.join(result))

# board = input()

# board = board.replace("XXXX", "AAAA")
# board = board.replace("XX", "BB")

# if 'X' in board:
#     print(-1)
    
# else:
#     print(board)