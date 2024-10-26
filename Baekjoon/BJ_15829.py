# print(26*31**0 + 26*31**1 + 26*31**2)
# print(ord('z')-96)

N = int(input())
alphabets = list(input())

r = 31  # given r from the problem
M = 1234567891  # given M from the problem
result = 0  # initialize 'result'
for i in range(N):
    a = ord(alphabets[i]) - 96
    result += a * (r ** i)

print(result % M)