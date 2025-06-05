T = int(input())
N = int(input())
tastes = list(map(int, input().split()))

if sum(tastes) >= T:
    print('Padaeng_i Happy')
else:  # sum(tastes) < T:
    print('Padaeng_i Cry')