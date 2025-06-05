import sys

N = sys.stdin.readline()
A = list(sys.stdin.readline().split())
B = list(sys.stdin.readline().split())

X = int(''.join(A))
Y = int(''.join(B))

if X >= Y:
    print(Y)
else:  # X < Y:
    print(X)