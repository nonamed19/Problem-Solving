import sys
input = sys.stdin.readline


N = int(input())

result = 0
for _ in range(N):
    words = input().strip()

    group, consecutive = [], True
    for word in words:
        if word not in group:
            group.append(word)
        else:  # if word in group:
            if word == group[-1]:
                pass
            else:
                consecutive = False
                break

    if consecutive is True:
        result += 1

print(result)
