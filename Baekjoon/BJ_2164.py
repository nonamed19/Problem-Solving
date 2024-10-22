from collections import deque

N = int(input())
numbers = deque(range(1, N + 1))

if len(numbers) == 1:
    numbers += [1]

while len(numbers) > 2:
    numbers.popleft()
    numbers.append(numbers.popleft())

numbers.popleft()
print(*numbers)