order = 0
while True:
    order += 1
    words1, words2 = input(), input()

    if words1 == 'END' and words2 == 'END':
        break

    print(f'Case {order}: {'same' if sorted(words1) == sorted(words2) else 'different'}')
