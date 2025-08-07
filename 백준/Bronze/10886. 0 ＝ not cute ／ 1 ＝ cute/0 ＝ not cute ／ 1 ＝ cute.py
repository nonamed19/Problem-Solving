import sys

N = int(sys.stdin.readline())

positive = 0
negative = 0
for _ in range(N):
    survey = int(sys.stdin.readline())
    if survey == 1:
        positive += 1
    else:  # survey == 0:
        negative += 1

if positive > negative: print("Junhee is cute!")
else: print("Junhee is not cute!")