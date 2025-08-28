import sys
input = sys.stdin.readline

def croatian(words):
    alphabet = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
    if words == 'dz=':
        return 3
    elif words[:2] in alphabet:
        return 2
    else:
        return 1


words = input().strip()

result, i = 0, 0
while i <= len(words) - 1:
    count = croatian(words[i:i+3])
    i += count
    result += 1

print(result)
