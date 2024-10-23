def is_consecutive(numbers):
    validation = 0
    for number in numbers:
        if number == '6':
            validation += 1
        else:
            validation = 0

        if validation >= 3:
            return True
    return False


N = int(input())

result = 100
cnt = 0
while N > cnt:
    result += 1
    temp = []
    for i in range(len(str(result))):
        temp.append(str(result)[i])

    if is_consecutive(temp):
        cnt += 1

print(result)