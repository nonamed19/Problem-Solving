T = int(input()) # 노선 수 T ( 1 ≤ T ≤ 50 )

for tc in range(T):
    K, N, M = map(int, input().split())
    # 0번에서 출발해 종점인 N번 정류장까지 이동
    # 한번 충전으로 최대한 이동할 수 있는 정류장 수 K
    # 충전기가 설치된 M개의 정류장 번호
    M_list = list(map(int, input().split()))

    loc_now = 0
    loc_station = 0
    flag_station = 0
    count = -1

    while count <= 100:
        count += 1
        for station in M_list:
            if station <= loc_now:
                loc_station = station
        # 현재 위치를 충전기가 설치된 정류장으로 변경
        loc_now = loc_station
        # 충전기가 설치된 정류장에서 거리 K 이동
        loc_now += K

        # 종료 조건
        if loc_now >= N:
            break

    if count != 101:
        print('#%d %d' %(tc+1, count))
    else:
        print('#%d %d' %(tc+1, 0))