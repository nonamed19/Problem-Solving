import sys; input = sys.stdin.readline


order = 0
while True:
    order += 1
    words1 = list(input().strip())
    words2 = list(input().strip())

    if words1 == list('END') and words2 == list('END'):
        break

    if len(words1) == len(words2):
        for word2 in words2:
            if word2 in words1:
                words1.remove(word2)
        if len(words1) == 0:
            print(f'Case {order}: same')
        else:
            print(f'Case {order}: different')
    else:
        print(f'Case {order}: different')
