T = int(input())

def del_iter(lst):
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            lst.pop(i+1)
            lst.pop(i)
            validation = True
            return lst, validation
    else:
        validation = False
        return lst, validation

for tc in range(T):
    lst = list(input())
    validation = True

    while validation :
        lst, validation = del_iter(lst)

    print('#%d %d' %(tc+1, len(lst)))