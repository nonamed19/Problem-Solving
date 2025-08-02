# N개의 자연수 중에서 M개를 고른 수열

import sys
from itertools import *

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers = sorted(numbers)

for temp in permutations(numbers, M):
    print(*temp)