T = 10

for tc in range(T):
    N = int(input()) # 문자열 계산식의 길이
    lst_str = input()
    lst = list(0 for _ in range(N))
    for i in range(N):
        lst[i] = lst_str[i]

    stack = []
    stack_oper = []
    operation = 0
    # 후위 표기식으로 변경
    for word in lst:
        if word == '+':
            if operation == 0:
                stack_oper.append(word)
                operation += 1
            else: # 사칙연산이 연속으로 등장하는 경우
                print('operation location error')
                break
        else:
            stack.append(int(word))
            if operation > 0:
                stack.append(stack_oper.pop())
                operation -= 1

    arr = []
    # 후위 표기식 계산
    for word in stack:
        if word != '+':
            arr.append(word)
        else:
            calc2 = arr.pop()
            calc1 = arr.pop()
            arr.append(calc1+calc2)
    
    if len(arr) == 1:
        print('#%d %d' %(tc+1, arr[0]))
    else:
        print('#%d arr 에러 발생' %(tc+1))



