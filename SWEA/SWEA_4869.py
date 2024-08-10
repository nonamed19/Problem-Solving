# solved through recursive function
T = int(input())

def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return f(n-1) + 2*f(n-2)

for tc in range(T):
    N = int(input())/10

    print('#%d %d' %(tc+1, f(N)))