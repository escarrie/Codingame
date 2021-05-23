import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
lines = [input() for _ in range(height)]

def find_right(x, y):
    for i in range(x + 1, width):
        if lines[y][i] == '0':
            return i, y
    return -1, -1

def find_bottom(x, y):
    for i in range(y + 1, height):
        if lines[i][x] == '0':
            return x, i
    return -1, -1

for y in range(height):
    for x in range(width):
        if lines[y][x] == '0':
            rx, ry = find_right(x, y)
            bx, by = find_bottom(x, y)
            print(x, y, rx, ry, bx, by)
