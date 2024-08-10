T = int(input())

for tc in range(T):
    lst = input()
    stack = []
    validation = 0

    for word in lst:
        if word == '(':
            stack.append(word)
        elif word == '{':
            stack.append(word)
        elif word == ')':
            if stack:
                temp = stack.pop()
                if temp != '(':
                    validation += 1
                    break
            else:
                validation += 1
                break
        elif word == '}':
            if stack:
                temp = stack.pop()
                if temp != '{':
                    validation += 1
                    break
            else:
                validation += 1
                break
        else:
            continue

    if stack:
        validation += 1

    if validation == 0:
        print('#%d %d' %(tc+1, 1)) # 참인 경우
    else:
        print('#%d %d' %(tc+1, 0)) # 거짓인 경우