import sys

try:
    data = open("Problem Set 6/E.txt")
except FileNotFoundError:
    data = sys.stdin


test_cases = int(data.readline())
for line in data:
    line = line.strip().split()
    n,k = int(line[0]),int(line[1])
    print(k ^ (k >> 1))
