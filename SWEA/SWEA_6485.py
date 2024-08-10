T = int(input())

for tc in range(T):
    N = int(input())
    Ai = [0]*N
    Bi = [0]*N
    for i in range(N):
        Ai[i], Bi[i] = map(int, input().split())

    P = int(input())
    Pi = [0]*P
    for i in range(P):
        Pi[i] = int(input())

    temp = [0]*P
    for i in range(P):
        for j in range(N):
            if Ai[j] <= Pi[i] <= Bi[j]:
                temp[i] += 1

    print('#%d' %(tc+1), end=' ')
    print(*temp)