# 정수 세 개가 주어졌을 때, 가장 작은 수, 그 다음 수, 가장 큰 수를 출력하는 프로그램을 작성하시오.

import sys

numbers = list(map(int, sys.stdin.readline().split()))
numbers = sorted(numbers)

print(*numbers)