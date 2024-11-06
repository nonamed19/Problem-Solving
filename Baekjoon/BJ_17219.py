import sys

N, M = map(int, sys.stdin.readline().split())

sites = {}
for _ in range(N):
    site, password = sys.stdin.readline().split()
    sites[site] = password

for _ in range(M):
    target = sys.stdin.readline()
    print(sites[target.strip()])