# 정수 A, B 가 주어진다.
# 세로 길이가 A cm, 가로 길이가 B cm 인 아래와 같은 직사각형의 넓이를 cm2 단위로 구하시오.

# 세로 길이가 A cm, 가로 길이가 B cm인 직사각형의 넓이를 cm2 단위로 구하고, 단위 (cm2)를 생략하여 출력한다.

import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())

area = A * B
print(area)