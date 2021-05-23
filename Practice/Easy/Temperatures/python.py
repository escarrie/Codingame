import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
t = []
for i in input().split():
    t.append(int(i))
i = 0
mini = 10000
while (i < len(t)):
    if (t[i] > 0 and mini > 0):
        if t[i] < mini:
            mini = t[i]
    elif (t[i] < 0 and mini > 0):
        if (-t[i] < mini):
            mini = t[i]
    elif (t[i] > 0 and mini < 0):
        if (t[i] < -mini or t[i] == -mini):
            mini = t[i]
    elif (t[i] < 0 and mini < 0):
        if (-t[i] < -mini):
            mini = t[i]
    elif (t[i] == 0):
        mini = 0
    i += 1
if (len(t) == 0):
    mini = 0
print(mini)
