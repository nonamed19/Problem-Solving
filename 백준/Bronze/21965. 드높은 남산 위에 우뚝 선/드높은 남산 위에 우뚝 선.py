import sys
input = sys.stdin.readline


N = int(input())

A = 0
mountains = map(int, input().split())
slope = True
ismountain = 'YES'
for mountain in mountains:
    # 증가하는 수열
    if slope:
        if A < mountain:
            A = mountain
        else:
            slope = False
    # 감소하는 수열
    else:  # if not slope:
        if mountain < A:
            A = mountain
        else:
            ismountain = 'NO'
            break

print(ismountain)
