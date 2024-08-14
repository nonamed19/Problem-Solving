T = 10

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(str, input()))
    lst_new = []
    stack = []

    for i in range(len(lst)):
        if lst[i] == '+':
            stack.append('+')
        elif lst[i] == '*':
            lst_new.append(lst[i-1])
            stack.insert(0, '*')
        else:
