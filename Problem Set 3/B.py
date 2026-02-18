import sys

try:
    data = open("Problem Set 3/B.txt")
except FileNotFoundError:
    data = sys.stdin



for line in data:
    line = line.strip().split()
    hand = line[:5]
    deck = line[5:]

    #print(hand, deck)
    for i in range(32):
        temp_hand = hand.copy()
        binary = list(bin(i)[2:].zfill(5))
        indices = [i for i in range(len(binary)) if binary[i] == '1']

        for i in range(len(indices)):
            hand[indices[i]] = deck[i]
        
        print(hand)
        suit_to_num = {}
        num_to_suit = {}



    print()