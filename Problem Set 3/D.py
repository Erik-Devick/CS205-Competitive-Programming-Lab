import sys

try:
    data = open("Problem Set 3/D.txt")
except FileNotFoundError:
    data = sys.stdin

def dfs(grid,r,c, counter):
    grid[r][c] = '*'
    #print(grid)
    to_check = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for loc in to_check:
        try:
            if grid[r+loc[0]][c+loc[1]] == '@':
                dfs(grid,r+loc[0],c+loc[1],counter)
        except IndexError:
            pass
    return grid, counter+1

for line in data:
    line_list = line.split()
    #print(line_list)
    if len(line_list) == 2:
        grid = []
        counter = 0
        rows, cols = int(line_list[0]), int(line_list[1])
        if (rows,cols) == (0,0):
            break
    else:
        grid.append(list(line_list[0]))
    if len(grid) == rows:
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    grid,counter = dfs(grid,r,c,counter)

        print(counter)




    
