order = 0
while True:
    order += 1
    flag = True
    words1, words2 = input(), input()

    if words1 == 'END' and words2 == 'END':
        break

    words1, words2 = sorted(words1), sorted(words2)

    if len(words1) == len(words2):
        for i in range(len(words1)):
            if words1[i] != words2[i]:
                flag = False
    else:
        flag = False

    if flag:
        print(f'Case {order}: same')
    else:
        print(f'Case {order}: different')
