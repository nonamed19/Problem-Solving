def perm(num, lst, visited):
    def calculate(num1, num2, oper):
        if oper == '+':
            return num1 + num2
        elif oper == '-':
            return num1 - num2
        elif oper == '*':
            return num1 * num2
        else:  # oper == '/':
            return num1 / num2

    if len(temp) == N-1:


        return

    for i in range(N-1):
        if visited[i]:
            continue

        visited[i] = 1
        temp.append(lst_oper[i])
        perm(num + 1, lst_num, visited)
        temp.pop()
        visited[i] = 0


T = int(input())

for tc in range(T):
    N = int(input())
    lst_oper_cnt = list(map(int, input().split()))
    lst_oper_exp = ['+', '-', '*', '/']
    lst_oper = []
    for i in range(4):
        lst_oper += [lst_oper_exp[i]]*lst_oper_cnt[i]
    lst_num = list(map(int, input().split()))

    lst, temp = [], []
    visited = [0]*(N-1)
    perm(0, temp, lst_num[:], visited)

    # print(lst)