A, B, C = map(int, input().split())
D = int(input())

# second
C += D

# minute
temp = C // 60
C -= temp * 60
B += temp

# hour
temp = B // 60
B -= temp * 60
A += temp
A %= 24

print(A, B, C)
