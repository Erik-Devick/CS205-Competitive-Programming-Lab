

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

#print(words)
two_compound_words = []
for word in words:
    if len(word) == 1:
        pass
    else:
        for i in range(len(word)-1):
            first_piece = word[:i+1]
            if first_piece in words:
                second_piece = word[i+1:]
                if second_piece in words:
                    two_compound_words.append(word)
                    break
            else:
                pass

#print(two_compound_words)
for word in two_compound_words:
    print(word)