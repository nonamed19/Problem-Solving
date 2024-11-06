import sys
from collections import deque


T = int(sys.stdin.readline())

for _ in range(T):
    p = list(sys.stdin.readline().strip())  # 수행할 함수 p
    n = int(sys.stdin.readline())
    numbers = sys.stdin.readline()[1:-2]

    if n:
        numbers = deque(map(int, numbers.split(',')))
    else:
        numbers = deque()

    reversed = False
    for command in p:
        # # pruning
        # if p.count('D') > len(numbers):
        #     numbers = 'error'
        #     break

        if command == 'R':
            reversed = not reversed
        elif command == 'D':
            if numbers:
                if reversed:
                    numbers.pop()
                else:
                    numbers.popleft()
            else:
                numbers = 'error'
                break

    if reversed:
        numbers.reverse()

    if not numbers == 'error':
        print(f'[{",".join(map(str, numbers))}]')
    else:
        print(numbers)
