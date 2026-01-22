import sys


try:
    data = open("Problem Set 2/D.txt")
except FileNotFoundError:
    data = sys.stdin


num_cases = int(data.readline())
for i in range(num_cases):
    unknown = ['A','B','C','D','E','F','G','H','I','J','K','L']
    real = []

    first_check = data.readline().split()
    if first_check[2] == "even":
        set1 = [char for char in first_check[0]]
        set2 = [char for char in first_check[1]]
        for coin in set1:
            if coin in unknown:
                unknown.remove(coin)
                real.append(coin)
        for coin in set2:
            if coin in unknown:
                unknown.remove(coin)
                real.append(coin)
                if first_check[2] == "even":
    for coin in set1:
        if coin in unknown:
            unknown.remove(coin)
            real.append(coin)
    for coin in set2:
        if coin in unknown:
            unknown.remove(coin)
            real.append(coin)
        
    print(unknown)
    print(real)
