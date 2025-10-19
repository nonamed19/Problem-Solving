T = int(input())

for _ in range(T):
    M, problem = input().split()
    words = input().split()

    result = []
    if problem == 'C':
        for word in words:
            result.append(ord(word) - 64)

    elif problem == 'N':
        for word in words:
            result.append(chr(int(word) + 64))

    print(*result)