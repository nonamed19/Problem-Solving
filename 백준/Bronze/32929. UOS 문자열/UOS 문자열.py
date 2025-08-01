words = ['U', 'O', 'S']

order = int(input())

result = words[order % 3 - 1]
print(result)