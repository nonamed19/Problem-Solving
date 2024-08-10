# solved through loop(for statement)
T = int(input())

for tc in range(T):
    N = int(int(input())/10)
    lst = [1, 3]

    for i in range(2, N):
        lst.append(lst[i-1] + 2*lst[i-2])

    print('#%d %d' %(tc+1, lst.pop()))