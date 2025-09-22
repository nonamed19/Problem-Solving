alphabets = str(input())

results = [['.' for _ in range((4 * len(alphabets) + 1) if len(alphabets) > 1 else 5)] for _ in range(5)]

# 피터팬 프레임
for i in range(len(alphabets)):
    if (i+1)%3 == 0:
        pass
    else:
        results[0][2 + i*4] = '#'
        results[1][1 + i*4], results[1][3 + i*4] = '#', '#'
        results[2][0 + i*4], results[2][2 + i*4], results[2][4 + i*4] = '#', alphabets[i], '#'
        results[3][1 + i*4], results[3][3 + i*4] = '#', '#'
        results[4][2 + i*4] = '#'

# 3의 배수 위치, 웬디 프레임
for i in range(len(alphabets)):
    if (i+1)%3 == 0:
        results[0][2 + i*4] = '*'
        results[1][1 + i*4], results[1][3 + i*4] = '*', '*'
        results[2][0 + i*4], results[2][2 + i*4], results[2][4 + i*4] = '*', alphabets[i], '*'
        results[3][1 + i*4], results[3][3 + i*4] = '*', '*'
        results[4][2 + i*4] = '*'

for result in results:
    print(*result, sep='')
