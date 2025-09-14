import sys; input = sys.stdin.readline
from math import *

order = 1
while True:
    a, b, c = map(int, input().split())
    if (a + b + c) == 0:
        break

    print(f"Triangle #{order}")
    if a == -1:
        if c > b:
            print(f"a = {sqrt(c**2 - b**2):.3f}")
        else:
            print("Impossible.")
    elif b == -1:
        if c > a:
            print(f"b = {sqrt(c**2 - a**2):.3f}")
        else:
            print("Impossible.")
    elif c == -1:
        print(f"c = {sqrt(a**2 + b**2):.3f}")

    print(); order += 1
