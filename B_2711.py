# 다시해야됨

T = int(input())
S = []
for _ in range(T):
    idx, mis = input().split()
    S.append((int(idx), mis))

for idx, mis in S:
    corrected_string = mis[:idx-1] + mis[idx:]
    print(corrected_string)
