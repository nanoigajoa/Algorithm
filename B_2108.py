import sys
from collections import Counter
input = sys.stdin.readline

def find_mode(num_list):
    count = Counter(num_list)
    max_freq = max(count.values())
    modes = [key for key, freq in count.items() if freq == max_freq]
    modes.sort()
    if len(modes) > 1:
        return modes[1]
    else:
        return modes[0]

N = int(input())
num = [int(input()) for _ in range(N)]
S_num = sorted(num)

print(int(round(sum(num)/len(num), 0))) # 산술평균
print(S_num[int(round(len(num)/2, 1) - 0.5)]) # 중앙값
print(find_mode(num))
print(S_num[-1] - S_num[0]) # 범위