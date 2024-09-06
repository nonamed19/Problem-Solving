def merge_sort(m):
    global cnt
    if len(m) == 1:
        return m

    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    if left[-1] > right[-1]:
        cnt += 1

    return merge(left, right)


def merge(left, right):
    result = [0] * (len(left) + len(right))
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    while l < len(left):
        result[l + r] = left[l]
        l += 1

    while r < len(right):
        result[l + r] = right[r]
        r += 1

    return result


T = int(input())

for tc in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0

    lst = merge_sort(lst)
    print(f'#{tc+1} {lst[N//2]} {cnt}')