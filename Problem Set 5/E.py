import sys

try:
    data = open("Problem Set 5/E.txt")
except FileNotFoundError:
    data = sys.stdin


big_grid = []
small_grid = []
for line in data:
    line_list = line.split()
    if len(line_list) == 2:
        r1,r2 = int(line_list[0]), int(line_list[1])
        big_grid = []
        small_grid = []
    else:
        line_list = list(line_list[0])
        print(line_list)



