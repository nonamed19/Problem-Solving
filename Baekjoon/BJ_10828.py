N = int(input())

stack = []
for _ in range(N):
    command = input().split()

    if command[0] == 'push':
        stack.append(int(command[1]))

    elif command[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif command[0] == 'size':
        if stack:
            print(len(stack))
        else:
            print(0)

    elif command[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)

    elif command[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)