import sys
import math

try:
    data = open("Problem Set 5/A.txt")
except FileNotFoundError:
    data = sys.stdin

for line in data:
    line = line.split()
    R,C = int(line[0]),int(line[1])
    if R == 0 and C == 0:
        break
    m = min(R,C)
    
    total = R*(C**2-C)+C*(R**2-R)+2*(abs(R-C)+1)*(m)*(m-1)+((4*m*(m-1)*(m-2))//3)
    print(int(total))