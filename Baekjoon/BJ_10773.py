N = int(input())

queue = []
for _ in range(N):
    number = int(input())
    if number != 0:
        queue.append(number)
    else:
        queue.pop()

print(sum(queue))