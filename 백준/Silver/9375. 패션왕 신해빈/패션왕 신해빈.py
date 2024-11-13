import sys

T = int(sys.stdin.readline())

for tc in range(T):
    n = int(sys.stdin.readline())

    clothes_list = []
    for _ in range(n):
        clothes_list.append(sys.stdin.readline().strip().split())

    clothes_types = []
    for i in range(n):
        clothes_types.append(clothes_list[i][1])
    clothes_types = list(set(clothes_types))

    clothes_dict = {}  ## dict.value를 list로
    for i in range(len(clothes_types)):
        clothes_dict[clothes_types[i]] = []
        for j in range(len(clothes_list)):
            if clothes_types[i] == clothes_list[j][1]:
                clothes_dict[clothes_types[i]].append(clothes_list[j][0])

    result = 1
    for clothes in clothes_dict:
        result *= len(clothes_dict[clothes]) + 1

    print(result - 1)