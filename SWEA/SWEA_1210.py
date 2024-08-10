from pprint import pprint

T = 1 # 10개의 테스트 케이스 / 수정 필요

for tc in range(T):
    N = int(input()) # number of test case
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = 2

