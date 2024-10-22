N = int(input())

persons = []
for _ in range(201):  # 1 <= N <= 200
    persons.append([])

for _ in range(N):
    age, name = input().split()
    persons[int(age)].append(name)

for i in range(len(persons)):
    if persons[i]:
        for j in range(len(persons[i])):
            print(i, persons[i][j])