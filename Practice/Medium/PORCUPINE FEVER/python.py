import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
y = int(input())
sick = [0] * n
healthy = [0] * n

for i in range(n):
    sick[i], healthy[i], _ = [int(j) for j in input().split()]

for year in range(y):
    for i in range(n):
        newsick = min(sick[i]*2, healthy[i])
        sick[i], healthy[i] = newsick, healthy[i] - newsick

    print(sum(sick + healthy))
    if sum(sick + healthy) == 0:
        break
