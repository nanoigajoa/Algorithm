A = int(input())
B = input() # 문자열은 문자열을 구성하는 문자에 접근할 수 있다(A만 정수변환)
 
print(A*int(B[2]))
print(A*int(B[1]))
print(A*int(B[0]))
print(A*int(B))