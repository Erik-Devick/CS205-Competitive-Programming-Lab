#ACCEPTED

import random
import sys


try:
    data = open("Problem Set 1/C.txt")
except FileNotFoundError:
    data = sys.stdin


num_cases = int(data.readline().strip())
letter_to_symbol = {
    'R' : '/',
    'C' : '_',
    'F' : '\\'
}

for case in range(num_cases):
    print(f"Case #{case+1}:")
    string = data.readline().strip()
    length = len(string)
    row = ['' for _ in range(length+2)]
    base_graph = [row.copy() for _ in range(101)]
    current_cell = (51,0)  #row, col
    for i in range(length):
        symbol = letter_to_symbol[string[i]]
        base_graph[current_cell[0]][current_cell[1]] = symbol
        current_cell = (current_cell[0],current_cell[1]+1)
        if symbol == "/":
            try:
                next_symbol = letter_to_symbol[string[i+1]]
            except IndexError:
                break
            if next_symbol == "\\":
                current_cell = (current_cell[0],current_cell[1])
            else:
                current_cell = (current_cell[0]-1,current_cell[1])

        if symbol == "_":
            try:
                next_symbol = letter_to_symbol[string[i+1]]
            except IndexError:
                break
            if next_symbol == "\\":
                current_cell = (current_cell[0]+1,current_cell[1])
            else:
                current_cell = (current_cell[0],current_cell[1])    

        if symbol == "\\":
            try:
                next_symbol = letter_to_symbol[string[i+1]]
            except IndexError:
                break

            if next_symbol == "\\":
                current_cell = (current_cell[0]+1,current_cell[1])
            else:
                current_cell = (current_cell[0],current_cell[1])

    base_graph = [row for row in base_graph if ''.join(row).strip() != '']
    final_graph = []
    for row in base_graph:
        while row[-1] == '':
            row = row[:-1]
        final_graph.append(row)
        #print(row)

    graph_string = ""
    for row in final_graph:
        #print(row)
        graph_string += "| "
        for cell in row:
            
            if cell == '':
                graph_string += " "
            else:
                graph_string += cell
        graph_string += '\n'
    graph_string += "+"+"-"*(length+2)

    final_string = ""
    print(graph_string)
    print()
    #print(repr(graph_string))
'''
letters = ['R','C','F']
string = ""
for i in range(50):
    
    string += random.choice(letters)
print(string)
'''