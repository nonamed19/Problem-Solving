def decrypt(word):
    ratio1, ratio2, ratio3 = 0, 0, 0
    word = word.lstrip('0') # 1부터 counting할 것

    while word[0] == '1':
        ratio1 += 1
        word = word[1::]
    while word[0] == '0':
        ratio2 += 1
        word = word[1::]
    while word[0] == '1':
        ratio3 += 1
        word = word[1::]

    # normalize
    while ratio1 / 2 >= 1:
        ratio1 /= 2
        ratio2 /= 2
        ratio3 /= 2

    print(ratio1, ratio2, ratio3)



T = int(input())

my_dict = {'211': 0, '221': 1, '122': 2, '411': 3, '132': 4,
           '231': 5, '114': 6, '312': 7, '213': 8, '112': 9}

for tc in range(T):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    for i in range(N):
        # 암호 코드 판별을 위한 16진수 숫자 탐색
        temp = arr[i].lstrip('0')
        binary_temp = ''
        while temp:
            temp1 = format(int(temp[0], 16), 'b')
            while len(temp1) < 4:
                temp1 = '0' + temp1
            binary_temp += temp1
            if len(temp) >= 2:
                temp = temp[1::]
            elif len(temp) == 1:
                break
            if temp[0] == '0':
                temp.lstrip('0')
        print(binary_temp)
        # 암호 코드 해독을 위한 '1' and '0' 비율 판별
        cnt = 0  # 해당 cnt가 8이 되면 함수 종료
        if binary_temp:
            decrypt(binary_temp)










# T = int(input())
#
# my_dict1 = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
#             '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
#
# for tc in range(T):
#     N, M = map(int, input().split())
#     arr = [list(input()) for _ in range(N)]
#
#     password_16 = []
#     temp = []
#     step = 0
#     for i in range(N):
#         for j in range(M-1, -1, -1):
#             # 15 BIT 16진수인 경우
#             if arr[i][j] != '0' and arr[i][j-15] == '0':
#                 temp.append(arr[i][j-14:j+1])
#                 for k in range(16):
#                     arr[i][j-k] = '0'
#             # 31 BIT 16진수인 경우
#             elif arr[i][j] != '0' and arr[i][j-31] == '0':
#                 temp.append(arr[i][j-30:j+1])
#                 for k in range(32):
#                     arr[i][j-k] = '0'
#
#     for x in temp:
#         if x not in password_16:
#             password_16.append(x)
#     # print(password_16)
#
#     password_2 = []
#     temp4 = ''
#     for lst in password_16:
#         for element in lst:
#             temp1 = format(int(element, 16), 'b')
#             while len(temp1) < 4:
#                 temp1 = '0' + temp1
#             temp4 += temp1
#         password_2.append(temp4)
#     # print(password_2)
#
#     # password_2 = []
#     # for lst in password_16:
#     #     temp1 = ''
#     #     for element in lst:
#     #         temp1 += my_dict[element]
#     #     password_2.append(temp1)
#     # print(password_2)
#
#     # 뒤에서부터 1을 찾은 뒤, 우측부터 1까지의 거리만큼 좌-우 0의 개수를 삭제
#     for i in range(len(password_2)):
#         order = 0
#         for j in range(60-1, -1, -1):
#             if password_2[i][j] == '1':
#                 break
#             else:
#                 order += 1
#         password_2[i] = password_2[i][(4-order):60-order]
#
#     codes = []
#     for i in range(len(password_2)):
#         temp2 = []
#         for j in range(8): # 7 * 8 = 56
#             temp3 = password_2[i][j*7:(j+1)*7]
#             temp2.append(my_dict1[temp3])
#         codes.append(temp2)
#
#     result = 0
#     for i in range(len(codes)):
#         odd = codes[i][0] + codes[i][2] + codes[i][4] + codes[i][6]
#         even = codes[i][1] + codes[i][3] + codes[i][5]
#         check = codes[i][7]
#         if (odd*3 + even + check) % 10 == 0:
#             result = odd + even + check
#             break
#
#     print(f'#{tc+1} {result}')