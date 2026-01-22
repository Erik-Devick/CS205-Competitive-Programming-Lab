import sys


try:
    data = open("Problem Set 2/C.txt")
except FileNotFoundError:
    data = sys.stdin


num_cases = int(data.readline())
for i in range(num_cases):
    count = 0
    string = data.readline()
    string_list = list(string)
    #print(string_list)
    #print(string_list)
    for letter in string_list:
        if letter in "adgjmptw":
            count += 1
        elif letter in "behknqux":
            count += 2
        elif letter in "cfilorvy":
            count += 3
        elif letter in "sz":
            count += 4
        elif letter == ' ':
            count += 1
    print(f"Case #{i+1}: {count}")