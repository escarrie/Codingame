import sys
import math

# game loop
while True:
    up = 0
    ind = 0
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        if (up < mountain_h):
            up = mountain_h
            ind = i
    print(ind)
