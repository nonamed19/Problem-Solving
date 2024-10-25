import sys

def binary_search(low, high):
    global result
    number = 0
    mid = (low + high) // 2
    for line in lines:
        number += line // mid

    # 종료 조건
    if low > high:
        return result

    if number < N:
        binary_search(low, mid - 1)
    else:  # number >= N:
        result = mid
        binary_search(mid + 1, high)


K, N = map(int, sys.stdin.readline().split())

lines = [0] * K
for i in range(K):
    lines[i] = int(sys.stdin.readline())

low, high = 1, max(lines) * 2  # initialization
binary_search(low, high)

print(result)