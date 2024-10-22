N = int(input())
numbers = list(map(int, input().split()))

numdict = {}
for number in numbers:
    if number in numdict:
        numdict[number] += 1
    else:
        numdict[number] = 1

M = int(input())
targets = list(map(int, input().split()))

result = []
for target in targets:
    if target in numdict:
        result.append(numdict[target])
    else:
        result.append(0)

print(*result)