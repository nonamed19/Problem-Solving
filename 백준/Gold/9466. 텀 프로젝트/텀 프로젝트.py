# 주어진 선택의 결과를 보고 어느 프로젝트 팀에도 속하지 않는 학생들의 수를 계산하는 프로그램을 작성하라.

import sys
sys.setrecursionlimit(10**5)  # (2 ≤ n ≤ 100,000)
input = sys.stdin.readline

def dfs(graph, v, visited):
    global count
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
        else:
            if not finished[i]:  # 사이클에 속한 전체 학생 수 누적(자기 자신도 포함)
                u, cnt = i, 1
                while graph[u][0] != i:
                    u = graph[u][0]
                    cnt += 1
                count += cnt
        finished[v] = True

T = int(input())
for _ in range(T):
    n = int(input())
    numbers = [0] + list(map(int, input().split()))

    students = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        students[i].append(numbers[i])

    count = 0
    visited = [False] * (n+1)
    finished = [False] * (n+1)  # finished를 통해 사이클을 계산해야 함
    for i in range(1, n+1):
        if not visited[i]:
            dfs(students, i, visited)

    print(n - count)
