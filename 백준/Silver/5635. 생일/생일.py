import sys
input = sys.stdin.readline


n = int(input())  # 1 <= n <= 100

students = [[name, int(month), int(day), int(year)] for name, month, day, year in (input().split() for _ in range(n))]
students.sort(key=lambda x: (x[3], x[2], x[1]))

# 가장 나이가 적은 사람의 이름
print(students[-1][0])

# 가장 나이가 많은 사람 이름
print(students[0][0])
