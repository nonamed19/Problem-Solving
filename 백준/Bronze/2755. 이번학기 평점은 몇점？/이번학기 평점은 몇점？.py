from decimal import Decimal, ROUND_HALF_UP

N = int(input())

grades = {
    "A+": 4.3, "A0": 4.0, "A-": 3.7,
    "B+": 3.3, "B0": 3.0, "B-": 2.7,
    "C+": 2.3, "C0": 2.0, "C-": 1.7,
    "D+": 1.3, "D0": 1.0, "D-": 0.7,
    "F": 0.0
}

scores, total = 0, 0
for _ in range(N):
    subject, score, grade = input().split()
    scores += int(score)
    total += grades[grade] * int(score)

GPA = Decimal(str(total / scores)).quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)
print(GPA)
