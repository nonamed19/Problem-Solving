import sys
input = sys.stdin.readline

N = int(input())

result = 0
prices = [0]*1001
expensive = 0
for i in range(N):
    name, cost = input().split()
    cost = int(cost)
    # 진주행 교통편인 경우
    if name == 'jinju':
        result = cost
    # 진주행 교통편이 아니고, 요금이 1000 이하(진주행 교통편 금액과 비교 필요)
    elif cost <= 1000:
        prices[cost] += 1
    # 진주행 교통편이 아니고, 요금이 1000 이상(반드시 진주행보다 비싼)
    else:
        expensive += 1

for i in range(result+1, 1001):
    expensive += prices[i]

print(result)
print(expensive)