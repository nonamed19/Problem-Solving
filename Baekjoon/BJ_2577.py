A = int(input())
B = int(input())
C = int(input())

mul = str(A * B * C)
result = [0] * 10

for num in mul:
    result[int(num)] += 1

for tem in range(len(result)):
    print(result[tem])