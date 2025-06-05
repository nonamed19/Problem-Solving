import sys

def calc(words):
    for i in range(len(words) - 2):
        if words[i] + words[i + 1] + words[i + 2] == 'BUG':
            words.pop(i + 2)
            words.pop(i + 1)
            words.pop(i)
            return words, False
    return words, True


sentences = sys.stdin.readlines()

for sentence in sentences:
    words = list(sentence.strip())

    flag = False
    while flag is not True:  # 'BUG'를 판별하고 제거하는 함수
        words, flag = calc(words)
        continue

    print(''.join(words))