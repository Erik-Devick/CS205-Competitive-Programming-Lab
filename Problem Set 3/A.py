import sys
import math


try:
    data = open("Problem Set 3/A.txt")
except FileNotFoundError:
    data = sys.stdin

point_sets = []
temp_set = []
while True:
    line = data.readline().strip().split()
    if len(line) == 1:
        point_sets.append(temp_set)
        temp_set = []
    else:
        temp_set.append(line)

    if line == []:
        break


point_sets.pop(0)
for set in point_sets:
    points = []
    for point in set:
        points.append((int(point[0]),int(point[1])))

    distances = []

    for i in range(len(points)):
        for j in range(len(points)):
            if i != j:
                distance = math.sqrt((points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2)
                distances.append(distance)
    
    try:
        if min(distances) >= 10000:
            print("INFINITY")
        else:
            print(round(min(distances),4))
    except:
        print("INFINITY")