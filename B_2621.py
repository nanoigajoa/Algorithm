import sys
input = sys.stdin.readline

card = []
score = 0

for i in range(5):
    card.append(input().split())
    
card.sort(key=lambda x : x[1])
# print(card)

for item in card:
    item[1] = int(item[1])

for j in range(4):
    if card[j][0] == card[j + 1][0]: # 카드가 같은색일때
        if card[j + 1][1] == card[j][1] + 1: # 숫자가 연속일때
            score += 900
            break
        else:
            score += 600
            break

print(score)