import sys
input = sys.stdin.readline

def track(A, B, C, P):
    score = (A * (B - P)**C)
    return int(score)

def field(A, B, C, P):
    score = (A * (P - B)**C)
    return int(score)

T = int(input())

for _ in range(T):
    P1, P2, P3, P4, P5, P6, P7 = map(int, input().split())

    result = (
            track(9.23076, 26.7, 1.835, P1) +
            field(1.84523, 75, 1.348, P2) +
            field(56.0211, 1.5, 1.05, P3) +
            track(4.99087, 42.5, 1.81, P4) +
            field(0.188807, 210, 1.41, P5) +
            field(15.9803, 3.8, 1.04, P6) +
            track(0.11193, 254, 1.88, P7)
            )

    print(result)
