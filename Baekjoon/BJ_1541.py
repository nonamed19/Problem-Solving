import sys

equations = sys.stdin.readline().strip()

numbers, operations, stacks = [], [], []
for equation in equations:
    if equation == '+' or equation == '-':
        operations.append(equation)
        numbers.append(int(''.join(stacks)))
        stacks = []
    else:
        stacks.append(equation)
numbers.append(int(''.join(stacks)))

order = 0
for operation in operations:
    if operation == '+':
        numbers[order] += numbers[order + 1]
        numbers.pop(order + 1)
    else:
        order += 1

if '-' in operations:
    print(numbers[0] - sum(numbers[1:]))
else:
    print(sum(numbers))