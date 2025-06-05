'''
대형 : 1
중형 : K
대형 : K * K

N = K^^2 + K + 1
N - 1 = K * (K + 1)
'''

def calc(N):
    for i in range(1, 101):
        if i * (i + 1) == N:
            return i


N = int(input()) - 1  # fire_medium + fire_small

print(calc(N))