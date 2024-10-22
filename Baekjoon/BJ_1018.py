from pprint import pprint

N, M = map(int, input().split())

colors = []
for _ in range(N):
    colors.append(list(input()))

result = 64
for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        temp = []
        cnt = 0
        for k in range(8):
            for l in range(8):
                temp.append(colors[i+k][j+l])

        for m in range(8):
            for n in range(4):
                if m % 2 == 0:
                    if temp[m*8 + n*2] == 'B':
                        cnt += 1
                    if temp[m*8 + (n*2)+1] == 'W':
                        cnt += 1
                else :
                    if temp[m*8 + n*2] == 'W':
                        cnt += 1
                    if temp[m*8 + (n*2)+1] == 'B':
                        cnt += 1

        cnt = min(cnt, 64 - cnt)
        result = min(result, cnt)

print(result)
