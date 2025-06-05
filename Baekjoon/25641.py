import sys
from collections import deque

N = sys.stdin.readline()
words = deque(sys.stdin.readline().strip())

while len(words) > 0:
    if words.count('s') == words.count('t'):
        print(''.join(words))
        break

    words.popleft()