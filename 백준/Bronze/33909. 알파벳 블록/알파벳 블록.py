S, C, O, N = map(int, input().split())

S += N
C += O*2

print(min(S//3, C//6))
