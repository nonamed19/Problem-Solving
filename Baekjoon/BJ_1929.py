N, K = map(int, input().split())

validation = [False, False] + [True]*(N-1)

primes = []
cnt = 0
for i in range(2, N+1):
  if validation[i]:
    primes.append(i)

    validation[i] = False
    cnt += 1
    if cnt == K:
        print(i)
        break

    for j in range(2*i, N+1, i):
        if validation[j] != False:
            validation[j] = False
            cnt += 1

            if cnt == K:
                print(j)
                break