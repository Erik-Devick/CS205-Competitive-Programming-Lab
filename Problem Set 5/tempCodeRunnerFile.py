import sys

try:
    data = open("Problem Set 5/C.txt")
except FileNotFoundError:
    data = sys.stdin

num_cases = int(data.readline())
for case in range(num_cases):
    string = list(data.readline().strip())
    strings_to_counts = []
    letter = ""
    count = ""
    for item in string:
        if not item.isnumeric():
            strings_to_counts.append((letter,count))
            letter = item
            count = ""
        else:
            count += item
    strings_to_counts.append((letter,count))
    strings_to_counts.pop(0)
    
    output = ""
    for pair in strings_to_counts:
        output += pair[0]*int(pair[1])
    print(f"Case {case+1}: {output}")
