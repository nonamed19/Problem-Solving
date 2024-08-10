T = int(input())

for i in range(T):
    n = int(input())
    lst = list(map(int, input().split()))

    if lst[0] > lst[1]:
        num_max = lst[0]
        num_min = lst[1]
    else:
        num_max = lst[1]
        num_min = lst[0]

    for j in range(n):
        if lst[j] > num_max:
            num_max = lst[j]
        if lst[j] < num_min:
            num_min = lst[j]

    print('#%d %d' %(i+1, (num_max - num_min)))