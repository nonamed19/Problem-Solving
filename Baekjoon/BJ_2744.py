words = list(input())

for i in range(len(words)):
    if words[i].isupper():
        words[i] = words[i].lower()
    else:
        words[i] = words[i].upper()
    print(words[i], end = '')