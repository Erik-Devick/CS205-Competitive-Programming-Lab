

import sys
import math


try:
    data = open("Problem Set 3/C.txt")
except FileNotFoundError:
    data = sys.stdin

words = []
while True:
    word = data.readline().strip()
    if word == '':
        break
    else:
        words.append(word)

first_letter_dict = {}
for word in words:
    first_letter = word[:1]
    if first_letter not in first_letter_dict.keys():
        first_letter_dict[first_letter] = [word]
    else:
        first_letter_dict[first_letter].append(word)

#print(words)
#print(first_letter_dict)

two_compound_words = []
for word in words:
    for i in range(len(word)-1):
        first_section = word[:i+1]
        second_section = word[i+1:]
        #print(first_section,second_section)
        if first_section in first_letter_dict[first_section[:1]]:
            if second_section in first_letter_dict[second_section[:1]]:
                two_compound_words.append(word)

for word in two_compound_words:
    print(word)