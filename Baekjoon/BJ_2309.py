def f():
    result = []
    for i in range(1, 4):
        for j in range(i + 1, 5):
            for k in range(j + 1, 6):
                for l in range(k + 1, 7):
                    for m in range(l + 1, 8):
                        for n in range(m + 1, 9):
                            for o in range(n + 1, 10):
                                if lst[i] + lst[j] + lst[k] + lst[l] + lst[m] + lst[n] + lst[o] == 100:
                                    result.append(lst[i])
                                    result.append(lst[j])
                                    result.append(lst[k])
                                    result.append(lst[l])
                                    result.append(lst[m])
                                    result.append(lst[n])
                                    result.append(lst[o])
                                    result = sorted(result)
                                    return result

temp = [0]
lst = [int(input()) for _ in range(9)]
lst = temp + lst

result = f()
for i in range(7): print(result[i])