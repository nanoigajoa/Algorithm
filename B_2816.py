N = int(input())
chnnal = [input() for _ in range(N)]
idx1, idx2 = chnnal.index('KBS1'), chnnal.index('KBS2')

if idx1 > idx2:
    idx2 += 1

print('1'*idx1 + '4'*idx1 + '1'*idx2 + '4'*(idx2-1))