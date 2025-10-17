N = int(input())

phrases = input()

counts = {}
for phrase in phrases:
    if phrase == ' ':
        continue

    if phrase not in counts:
        counts[phrase] = 1
    else:
        counts[phrase] += 1

print(max(counts.values()))