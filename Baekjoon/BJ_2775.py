T = int(input())

for tc in range(T):
    k = int(input())  # k층
    n = int(input())  # n호

    residents = []
    for i in range(1 + k):  # basement floor + kth floor
        for j in range(1, 14+1):  # n <= 14

            if (i*14) + j - 1 < 14:  # basement floor
                residents.append(j)

            else:  # (i*14) + j - 1 >= 14:  # above basement floor
                temp = 0
                for l in range(j):
                    temp += residents[((i-1)*14 + l)]
                residents.append(temp)

    print(residents[14*k + n - 1])