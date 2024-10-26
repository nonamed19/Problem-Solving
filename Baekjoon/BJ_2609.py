num1, num2 = map(int, input().split())

GCD = 0
for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        GCD = i

LCM = max(num1, num2)
while True:
    if LCM % num1 == 0 and LCM % num2 == 0:
        break
    LCM += 1

print(GCD)
print(LCM)