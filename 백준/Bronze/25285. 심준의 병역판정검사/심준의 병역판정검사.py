T = int(input())

for _ in range(T):
    height, weight = map(int, input().split())
    BMI = weight/(height/100)**2

    if 204 <= height:
        print(4)
    elif 161 <= height < 204:
        if 20 <= BMI < 25:
            print(1)
        elif 18.5 <= BMI < 20 or 25 <= BMI < 30:
            print(2)
        elif 16 <= BMI < 18.5 or 30 <= BMI < 35:
            print(3)
        elif BMI < 16 or 35 <= BMI:
            print(4)
    elif 159 <= height < 161:
        if 16 <= BMI < 35:
            print(3)
        elif BMI < 16 or 35 <= BMI:
            print(4)
    elif 146 <= height < 159:
        print(4)
    elif 140.1 <= height < 146:
        print(5)
    elif height < 140.1:
        print(6)
