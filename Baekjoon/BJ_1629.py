import sys
# sys.getrecursionlimit(100000)

A, B, C = map(int, sys.stdin.readline().split())

mul1 = A ** 1
mul2 = A ** 2
mul3 = A ** 3

idx1, idx2, idx3 = 0, 0, 0  # initialization
if B == 1:
    idx1 = 1
    result = mul1**idx1
else:
    if B % 2 == 0:
        idx2 = B // 2
        result = mul2**idx2
    else:
        idx2 = B // 2 - 1
        idx3 = 1
        result = mul2**idx2 * mul3**idx3

print(result % C)