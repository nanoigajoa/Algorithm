import statistics

L = []

for i in range(5):
    N = int(input())
    L.append(N)

aver = statistics.mean(L)
med = statistics.median(L)
print(aver)
print(med)