phrase = 'SciComLove'

N = int(input())
N %= len(phrase)

print(phrase[N:] + phrase[:N])
