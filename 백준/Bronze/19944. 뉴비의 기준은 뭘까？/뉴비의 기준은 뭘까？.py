N, M = map(int, input().split())

result = ''

if 1 <= M <= 2:
    result = 'NEWBIE!'
elif 3 <= M <= N:
    result = 'OLDBIE!'
else:
    result = 'TLE!'

print(result)