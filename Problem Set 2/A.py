import sys


try:
    data = open("Problem Set 2/A.txt")
except FileNotFoundError:
    data = sys.stdin

num_cases = int(data.readline())
for i in range(num_cases):
    stores = int(data.readline())
    store_positions = data.readline().split()
    #print(store_positions)
    store_positions = [int(pos) for pos in store_positions]
    store_positions = sorted(store_positions)
    #print(store_positions)

    distances_between_stores = []
    for i in range(stores):
        try:
            distances_between_stores.append(abs(store_positions[i]-store_positions[i+1]))
        except:
            pass
    #print(distances_between_stores)
    print(sum(distances_between_stores)*2)
