T = int(input()) # 테스트 케이스의 개수 T

for tc in range(T):
    N = int(input()) # N 은 5 이상 50 이하
    arr = list(map(int, input().split()))

    for i in range(N-1):
        idx_min = i
        for j in range(i+1, N):
            if arr[idx_min] > arr[j]:
                idx_min = j
        arr[i], arr[idx_min] = arr[idx_min], arr[i]

    print(f'#{tc+1} {" ".join(map(str, arr))}')