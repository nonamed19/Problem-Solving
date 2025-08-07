import sys

N = int(sys.stdin.readline())

result = 0
prices = []
for i in range(N):
    name, temp = sys.stdin.readline().split()
    if name == 'jinju':
        result = int(temp)
    else:
        prices.append(int(temp))

expensive = 0
for price in prices:
    if result < price:
        expensive += 1

print(result)
print(expensive)