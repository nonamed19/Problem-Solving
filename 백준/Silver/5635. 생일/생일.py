import sys
input = sys.stdin.readline


n = int(input())  # 1 <= n <= 100

names, dates = [], []
for _ in range(n):
    name, day, month, year = input().split()
    if len(day) == 1:
        day = '0' + day
    if len(month) == 1:
        month = '0' + month
    names.append(name)
    dates.append(year + month + day)

# 가장 나이가 적은 사람의 이름
print(names[dates.index(max(dates))])

# 가장 나이가 많은 사람 이름
print(names[dates.index(min(dates))])
