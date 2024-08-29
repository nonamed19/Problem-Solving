N = int(input())

for i in range(N):
    integer = i+1
    temp = list(str(integer))

    if ('3' in temp) or ('6' in temp) or ('9' in temp):
        for num in temp:
            if (num == '3') or (num == '6') or (num == '9'):
                print('-', end = '')
    else:
        print(integer, end = '')
    print(end = ' ')