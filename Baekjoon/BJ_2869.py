from math import ceil

A, B, V = map(int, input().split())

# 수식을 통해 최대한 가깝게 올려 보낸 뒤 반복문 수행
days = ceil(V / (A - B))
distance = (A - B) * days
days = days - A
distance = distance - (A - B)*A

while True:
    days += 1
    distance += A
    if distance >= V:
        print(days)
        break
    else:
        distance -= B