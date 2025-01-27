import sys
input = sys.stdin.readline

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
matrix2 = [list(map(int, input().split())) for _ in range(N)]

new_mat = [[] for _ in range(N)]
for i in range(N):
    for j in range(M):
        new_mat[i].append(matrix[i][j] + matrix2[i][j])

    print(* new_mat[i])