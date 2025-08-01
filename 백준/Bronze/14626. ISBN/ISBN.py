ISBN = list(input())
# ISBN = ['9', '7', '8', '8', '9', '6', '8', '3', '2', '2', '2', '7', '3']

order = ISBN.index('*')

ISBN.insert(order, '0')
ISBN.remove('*')
ISBN = list(map(int, ISBN))

sum_odd = sum(ISBN[0:12:2])
sum_even = sum(ISBN[1:12:2])

check = 10 - (sum_odd + sum_even) % 10

# '*'가 홀수 위치에 있는 경우
if order % 2 == 0:
    result = (10 - ISBN[12] - (sum_odd + sum_even*3)) % 10
# '*'가 짝수 위치에 있는 경우
else:
    result = abs((10 - ISBN[12] - (sum_odd + sum_even*3))*3) % 10

print(result)
