T = 10                                      # 총 10개의 테스트케이스가 주어진다.

for _ in range(T):
    n = int(input())                        # 건물의 개수 N이 주어진다. (4 ≤ N ≤ 1000)
    lst = list(map(int, input().split()))   # (0 ≤ 각 건물의 높이 ≤ 255)
    num_building = 0

    for i in range(2, n-2):
        building_height = 0

        if lst[i-2] > building_height:
            building_height = lst[i-2]
        if lst[i-1] > building_height:
            building_height = lst[i-1]
        if lst[i+1] > building_height:
            building_height = lst[i+1]
        if lst[i+2] > building_height:
            building_height = lst[i+2]

        if lst[i] > building_height:
            num_building += lst[i] - building_height

    print('#%d %d' %(_+1, num_building))