import os 
import csv


# create a function to open file  called read_file
def read_file(path):
    with open(path) as file:
        csvreader = csv.reader(file, delimiter=",")
        # remove header from data
        header = next(csvreader)
        data = []
        for row in csvreader:
            data.append(row)
    return data

# create a function to count vote, start with a blank dictionary and set initial total volume to 0
def count_vote(data):
    candidates = {}
    total_votes = 0

    for row in data:
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1
    return candidates

def calculate_result

vote_percents(candidates, total_votes):
    percents = {}
    for key, value in candidates.items():
        percents(candidate) = int(round((votes/total_votes)*100,0))
    return percents

print_results


print_candidates = ""
print_candidates = print_candidates + f"{candidate}"{votes} votes: ({int})



#print print_winner and then print_candidates 






def dothething(path):
    data = read_file(path)
    candidates, total_votes = count_vote(data)
    results = calculate_results(candidates, total_votes)
    print(results)
    
dothething("election_data.csv")