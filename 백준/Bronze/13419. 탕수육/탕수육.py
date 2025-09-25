T = int(input())

for _ in range(T):
    phrases = input()
    phrases = phrases if len(phrases) % 2 == 0 else phrases*2

    print(phrases[::2])
    print(phrases[1::2])
