import sys

# def fibonacci(number):
#     global output0, output1
#     if number == 0:
#         output0 += 1
#         return 0
#     elif number == 1:
#         output1 += 1
#         return 1
#     else:
#         return fibonacci(number - 1) + fibonacci(number - 2)


T = int(sys.stdin.readline())

for tc in range(T):
    N = int(sys.stdin.readline())
    list_for_0 = [1, 0]
    list_for_1 = [0, 1]

    for i in range(40):
        list_for_0.append(list_for_1[-1])
        list_for_1.append(list_for_0[-2] + list_for_0[-1])

    print(list_for_0[N], list_for_1[N])