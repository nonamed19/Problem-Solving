T = int(input())

for tc in range(T):
    lst = input().split()
    stack = []
    validation = 0

    for word in lst:
        if word == '+':
            if len(stack) >= 2:
                calc1 = stack.pop()
                calc2 = stack.pop()
                stack.append(calc2 + calc1) # pop이기 때문에 순서 유의
            else:
                validation += 1
        elif word == '-':
            if len(stack) >= 2:
                calc1 = stack.pop()
                calc2 = stack.pop()
                stack.append(calc2 - calc1) # pop이기 때문에 순서 유의
            else:
                validation += 1
        elif word == '*':
            if len(stack) >= 2:
                calc1 = stack.pop()
                calc2 = stack.pop()
                stack.append(calc2 * calc1) # pop이기 때문에 순서 유의
            else:
                validation += 1
        elif word == '/':
            if len(stack) >= 2:
                calc1 = stack.pop()
                calc2 = stack.pop()
                stack.append(calc2 / calc1) # pop이기 때문에 순서 유의
            else:
                validation += 1
        elif word == '.':
            break
        else:
            stack.append(int(word))

    if validation == 0 and len(stack) == 1:
        print('#%d %d' %(tc+1, stack[0]))
    else:
        print('#%d error' %(tc+1))