N = int(input())
note = []
for i in range(N):
    r, e, c = map(int, input().split())

    if e - c < r:
        note.append("do not advertise")
    elif e - c == r:
        note.append("does not matter")
    elif e - c > r:
        note.append("advertise")

print('\n'.join(map(str, note)))