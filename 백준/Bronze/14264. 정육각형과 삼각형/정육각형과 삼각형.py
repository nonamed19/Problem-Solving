import sys
from math import *
input = sys.stdin.readline

L = int(input())

h = (1/2)*L
b = sqrt(3)*h*2

area = b*h*(1/2)
print(area)
