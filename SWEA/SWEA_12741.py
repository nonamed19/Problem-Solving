T = int(input())
result = []

for tc in range(T):
    A, B, C, D = map(int, input().split())
    result += [max(0, min(B, D) - max(A, C))]

for i in range(T):
    print(f'#{i + 1} {result[i]}')