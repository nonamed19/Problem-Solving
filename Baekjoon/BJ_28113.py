N, A, B = map(int, input().split())
# N : 지하철 승강장까지 걸어가는 데에 걸리는 시간
# A : 현재 위치로 버스가 도착하는 데에 걸리는 시간
# B : 지하철 승강장으로 지하철이 도착하는 데에 걸리는 시간


if N <= B:  # 지하철을 탑승할 수 있는 경우 中
    if A < B:  # 버스가 더 빠른 경우
        print('Bus')
    elif A == B:
        print('Anything')
    else: # A > B:
        print('Subway')
else: # N > B:  # 지하철을 탑승할 수 없는 경우 中
    print('Bus')