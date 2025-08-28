import sys
input = sys.stdin.readline


words = input().strip()

alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for alphabet in alphabets:
    if alphabet in words:
        words = words.replace(alphabet, '*')

print(len(words))
