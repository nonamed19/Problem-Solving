N = int(input())

result = 0
for num in range(N-1, 0, -1):
    num_str = str(num)

    temp = num
    for i in range(len(num_str)):
        temp += int(num_str[i])

    if temp == N:
        result = num  # 분해합 재할당

print(result)