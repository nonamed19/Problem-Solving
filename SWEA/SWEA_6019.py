T = int(input())

for tc in range(T):
    D, A, B, F = map(float, input().split())

    print('#%d %f' %(tc+1, (D/(A+B)*F)))