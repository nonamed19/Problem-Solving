# 이런 유형의 문제는 dfs가 아니라 bfs로 풀어야 함
from collections import deque

def bfs(N, M, visited):
    q = deque()
    q.append(N)
    visited[N] = 0

    while True:
        temp = q.popleft()
        if temp == M:
            return visited[temp]

        num1 = temp + 1
        if 0 <= num1 < M + 11 and visited[num1] == -1:
            q.append(num1)
            visited[num1] = visited[temp] + 1
        num2 = temp - 1
        if 0 <= num2 < M + 11 and visited[num2] == -1:
            q.append(num2)
            visited[num2] = visited[temp] + 1
        num3 = temp * 2
        if 0 <= num3 < M + 11 and visited[num3] == -1:
            q.append(num3)
            visited[num3] = visited[temp] + 1
        num4 = temp - 10
        if 0 <= num4 < M + 11 and visited[num4] == -1:
            q.append(num4)
            visited[num4] = visited[temp] + 1


T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    visited = [-1]*(M+11)
    result = bfs(N, M, visited)

    print(f'#{tc+1} {result}')