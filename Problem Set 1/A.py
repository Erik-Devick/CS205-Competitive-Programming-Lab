import sys
import pathlib
import io

#Not sure about the best way to handle input files in competitive programming.
'''
if not sys.stdin.isatty():
    data = sys.stdin.read()
else:
    data = io.StringIO(pathlib.Path("Problem Set 1/A.txt").read_text())
'''

with open("Problem Set 1/A.txt", "r") as f:
    num_cases = int(f.readline().strip())
    for case in range(num_cases):
        num_candidates = int(f.readline().strip())
        candidates = []
        for _ in range(num_candidates):
            candidates.append((f.readline().strip(),0))
        
        newcase = False
        winner = False
        ballots = []
        while not newcase:
            ballot = f.readline().strip().split()
            #print(len(ballot))
            if len(ballot) == 0:
                newcase = True
                print(candidates)
                print(ballots)
                #find winner
                first_check = [0]*num_candidates
                for ballot in ballots:
                    first_check[int(ballot[0])-1] += 1
                #print(first_check)
                max_votes = max(first_check)
                if max_votes > len(ballots)/2 and first_check.count(max_votes) == 1:
                    winner = True
                    winning_index = first_check.index(max_votes)
                    print(candidates[winning_index][0])

            else:
                ballots.append(ballot)
