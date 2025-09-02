import sys
input = sys.stdin.readline


alphabets = input().strip()

words, counts = [], []
for alphabet in alphabets:
    alphabet = alphabet.upper()
    if alphabet not in words:
        words.append(alphabet)
        counts.append(1)

    elif alphabet in words:
        counts[words.index(alphabet)] += 1

max_count = max(counts)
max_word = words[counts.index(max_count)]
counts.remove(max_count)

if max_count in counts:
    print('?')
else:
    print(max_word)
