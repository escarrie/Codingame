import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(input())
chev = [0] * N
for i in range(N):
    Pi = int(input())
    chev[i] = Pi

chev.sort()

mini = 10**10
for i in range(N - 1):
    if (chev[i + 1] - chev[i]) < mini:
        mini = chev[i + 1] - chev[i]
print(str(mini)) 
