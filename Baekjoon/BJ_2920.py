lst = list(map(int, input().split()))

temp_lst = []
for i in range(len(lst) - 1):
    temp_lst.append(lst[i+1] - lst[i])

result = set(temp_lst)
if len(result) != 1:
    print('mixed')
else:
    temp = result.pop()
    if temp == 1:
        print('ascending')
    elif temp == -1:
        print('descending')
    else:
        print('mixed')