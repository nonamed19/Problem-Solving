import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

numbers_distinct = sorted(list(set(numbers)))
orders = list(range(N))

### 중복 제거 후 key -> value 추출은 list가 아니라 dictionary를 활용할 것 ###
numbers_dict = dict(zip(numbers_distinct, orders))

for number in numbers:
    print(numbers_dict[number])