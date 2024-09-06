T = int(input())

for tc in range(T):
    num_bin = list(map(int, input()))
    num_tri = list(map(int, input()))
    possible_bin = []
    possible_tri = []
    debugging_bin = [] # for debugging
    debugging_tri = [] # for debugging

    # for 2진수
    for i in range(len(num_bin)):
        temp = num_bin[:]
        for j in range(2):
            temp[i] = j
            debugging_bin.append(temp) # for debugging
            # 2진수 -> 10진수로 변경
            word = ''
            for k in range(len(num_bin)):
                word += str(temp[k])
            possible_bin.append(int(word, 2))

    # for 3진수
    for i in range(len(num_tri)):
        temp = num_tri[:]
        for j in range(3):
            temp[i] = j
            debugging_tri.append(temp) # for debugging
            # 3진수 -> 10진수로 변경
            word = ''
            for k in range(len(num_tri)):
                word += str(temp[k])
            possible_tri.append(int(word, 3))

    for num in possible_bin:
        if num in possible_tri:
            print(f'#{tc+1} {num}')
            break