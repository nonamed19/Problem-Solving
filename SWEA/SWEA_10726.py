T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    temp = format(M, 'b')

    while len(temp) <= 30:
        temp = '0' + temp

    if '0' in temp[-1:-(N+1):-1]:
        print(f'#{tc+1} OFF')
    else:
        print(f'#{tc+1} ON')