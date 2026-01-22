import sys
import pathlib
import io


if not sys.stdin.isatty():
    data = sys.stdin.read()
else:
    data = io.StringIO(pathlib.Path("Problem Set 1/D.txt").read_text())

def count_zeros_before(n):
    count = 0
    n_list  = list(str(n))
    place = len(n_list)
    index = 0
    
    while place > 0:
        digit = int(n_list[index])
        count += digit * ((place-1) * 10**(place-1))
        place -= 1
        index += 1

    return count

more = True
while more:
    int1, int2 = data.readline().strip().split()
    int1 = int(int1)
    int2 = int(int2)
    if int1 == -1 and int2 == -1:
        more = False
    else:
        print(count_zeros_before(int1), count_zeros_before(int2))

