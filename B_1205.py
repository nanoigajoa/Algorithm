import sys
input = sys.stdin.readline

N, tesu, P = map(int, input().split())

if N == 0:
    print(1)
else:
    point = list(map(int, input().split()))
    point.sort(reverse=True)

    for poi in point:
        if len(point) == P and tesu <= point[-1]:
            print(-1)
            break

        if tesu >= poi:
            print(point.index(poi)+1)
            # print("t")
            break

        if tesu == poi and len(point) < P:
            print(point.index(poi)+1)
            # print("실행결과-예제")
            break
        
        if tesu < point[-1] and len(point) < P:
            print(len(point)+1)
            # print("실행결과")
            break

        if tesu >= point[0] and len(point) < P:
            print(1)
            break