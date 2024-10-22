N = int(input())

for _ in range(N):
    stack = []
    temps = list(input())

    for temp in temps:
        stack.append(temp)

        if len(stack) >= 2:
            pop1 = stack.pop()
            pop2 = stack.pop()
            if pop2 == '(' and pop1 == ')':
                pass
            else:
                stack.append(pop2)
                stack.append(pop1)

    if stack:
        print('NO')
    else:
        print('YES')