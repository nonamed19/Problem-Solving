import sys
input = sys.stdin.readline

from collections import deque

def bfs(v, visited):
    queue = deque()
    queue.append(v)

    while queue:
        v = queue.popleft()

        if v == K:
            print(visited[v])
            break

        for move in (v-1, v+1, v*2):
            if 0 <= move <= max_num and not visited[move]:
                visited[move] = visited[v] + 1
                queue.append(move)


N, K = map(int, input().split())
max_num = 100000

visited = [0] * (max_num + 1)
bfs(N, visited)
