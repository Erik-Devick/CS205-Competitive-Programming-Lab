import sys
import math


try:
    data = open("Problem Set 3/C.txt")
except FileNotFoundError:
    data = sys.stdin

letter_count_dict = {}
words = []
while True:
    word = data.readline().strip()
    length = len(word)
    if word == "":
        break
    else:
        words.append(word)
    if length not in letter_count_dict.keys():
        letter_count_dict[length] = [word]
    else:
        letter_count_dict[length].append(word)

#print(letter_count_dict)
#print(letter_count_dict[11])

compound_words = []

for word in words:
    if len(word) == 1:
        pass
    else:
        lengths_to_check = []
        for i in range(len(word)):
            length_a = i
            length_b = len(word) - i
            if length_a != 0 and length_a < length_b:
                if length_a in letter_count_dict.keys() and length_b in letter_count_dict.keys():
                    lengths_to_check.append((length_a,length_b))
        #print(word, lengths_to_check)
        for checking_pair in lengths_to_check:
            for word1 in letter_count_dict[checking_pair[0]]:
                for word2 in letter_count_dict[checking_pair[1]]:
                    if word1 in word and word2 in word:
                        compound_words.append(word)

compound_words = list(set(compound_words))
compound_words = sorted(compound_words)
for word in compound_words:
    print(word)
