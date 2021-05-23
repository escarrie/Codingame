import sys
import math

n = int(input())
time = [0] * n
for i in range(n):
    time[i] = input()
time.sort()
print(time[0])
