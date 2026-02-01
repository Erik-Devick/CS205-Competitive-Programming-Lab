import sys

try:
    data = open("Problem Set 3/D.txt")
except FileNotFoundError:
    data = sys.stdin

rows,cols = data.readline().split()
rows,cols = int(rows),int(cols)
print(rows,cols)
field = []
for row in range(rows):
    
