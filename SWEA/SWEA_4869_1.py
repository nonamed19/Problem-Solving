# solved through memoization
T = int(input())

def f(N):
    global result
    if 2 < N:
        result[N] = f(N-1) + 2*f(N-2)
    return result[N]

for tc in range(T):
    N = int(int(input())/10)

    result = list(0 for _ in range(N+1))
    result[0] = 1
    result[1] = 1
    result[2] = 3

    print('#%d %d' %(tc+1, f(N)))