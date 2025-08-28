import sys
input = sys.stdin.readline


N = int(input())
P = int(input())

prices = [P]  # in case no discount is applied

if N >= 5:
    prices.append(P - 500)
if N >= 10:
    prices.append(P * 0.9)
if N >= 15:
    prices.append(P - 2000)
if N >= 20:
    prices.append(P * 0.75)

if min(prices) < 0:
    result = 0
else:
    result = int(min(prices))

print(result)
