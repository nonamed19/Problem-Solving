T = int(input())

for _ in range(T):
    phrases = input()
    length = len(phrases)

    # 입력 데이터의 개수가 짝수인 경우
    if length % 2 == 0:
        print(*[phrases[2*i] for i in range(length//2)], sep='')
        print(*[phrases[2*i+1] for i in range(length//2)], sep='')

    # 입력 데이터의 개수가 짝수인 경우
    else:  # elif length % 2 == 1:
        print(*[phrases[2*i] for i in range(length//2+1)] + [phrases[2*i+1] for i in range(length//2)], sep='')
        print(*[phrases[2*i+1] for i in range(length//2)] + [phrases[2*i] for i in range(length//2+1)], sep='')
