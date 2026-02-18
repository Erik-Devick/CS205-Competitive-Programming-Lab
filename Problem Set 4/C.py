import sys

try:
    data = open("Problem Set 4/C.txt")
except FileNotFoundError:
    data = sys.stdin


num_cases = int(data.readline())
vowels = "aeiou"
for i in range(num_cases):
    name1 = data.readline().strip()
    name2 = data.readline().strip()
    same = True
    #print(name1, name2)

    if len(name1) != len(name2):
        same = False
    else:
        for i in range(len(name1)):
            if name1[i] not in vowels and name2[i] != name1[i]:
                same = False
                break
            elif name1[i] in vowels and name2[i] not in vowels:
                same = False
            
    if same:
        print("Yes")
    else:
        print("No")