import sys

N, M = map(int, sys.stdin.readline().split())

set1 = set()
for i in range(N):
    set1.add(sys.stdin.readline())

set2 = set()
for i in range(M):
    set2.add(sys.stdin.readline())

results = list(set1.intersection(set2))
results.sort()

print(len(results))
for result in results:
    print(result[:-1])