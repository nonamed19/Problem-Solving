N = int(input())

number = 1
for i in range(1, N+1):
    number *= i

number = str(number)
cnt = 0
for i in range(len(number)-1, -1, -1):
    if number[i] != '0':
        print(cnt)
        break
    else:
        cnt += 1