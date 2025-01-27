import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
sensor = list(map(int, input().split()))
sensor.sort()

D = []
for i in range(1, N):
    D.append(sensor[i] - sensor[i - 1])
D.sort(reverse=True)
D = D[K-1::]

print(sum(D))