N = 3

strings = []
for _ in range(N):
    strings.append(input())

string, idx = 0, 0
for i in range(N):
    if strings[i].isdigit():
        string = int(strings[i])
        idx = i

target = string + (3 - idx)

if target % 3 == 0 and target % 5 == 0:
    print('FizzBuzz')
elif target % 3 == 0 and target % 5 != 0:
    print('Fizz')
elif target % 3 != 0 and target % 5 == 0:
    print('Buzz')
else:
    print(target)