N = int(input())
beads = input()

result, count = 0, 0
for bead in beads:
    if bead == '1':
        count += 1
    elif 0 < count:
        result += count*(count + 1) // 2
        count = 0

if 0 < count:
    result += count * (count + 1) // 2

print(result)
