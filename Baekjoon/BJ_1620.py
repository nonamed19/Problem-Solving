N, M = map(int, input().split())

pokemons = {}
for i in range(N):
    pokemons[i+1] = input()

pokemons_rev = {}
for key, value in pokemons.items():
    pokemons_rev[value] = key

for _ in range(M):
    target = input()
    if target.isnumeric():
        result = pokemons[int(target)]
    else:
        result = pokemons_rev[target]
    print(result)