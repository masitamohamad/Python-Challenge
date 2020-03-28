import os 
import csv

# Create a read_file function that reads a .csv file
def read_file(path):
    with open(path) as file:
        csvreader = csv.reader(file, delimiter=",")
        # remove header from data
        header = next(csvreader)
        data = []
        for row in csvreader:
            data.append(row)
    return data

# Create a count_vote function to count the total number of votes that each candidate received
def count_vote(data):
    
    # Initialize new variables. Set total votes to 0 and create empty dictionary to hold results
    candidate_dict = {}
    total_votes = 0

    # Iterate over each row of data table and update variables
    for row in data:
        candidate_name = row[2]
        total_votes += 1
        if candidate_name in candidate_dict:
            candidate_dict[candidate_name] += 1
        else:
            candidate_dict[candidate_name] = 1
    return [candidate_dict, total_votes]

# Create a calculate_result function that performs calculations to determine election winner
def calculate_results(candidate_dict, total_votes):
    
    # Initialize new variables
    winning_votes = 0
    winner = ""

    for candidate_name, votes in candidate_dict.items():
        if votes > winning_votes:
            winner = candidate_name
            winning_votes = votes
   
    # Prepare results data to print
    print_winner = f"Winner: {winner}"
    
    # Initialize new variable
    print_candidates = ""
    for candidate_name, votes in candidate_dict.items():
        print_candidates = print_candidates + f"{candidate_name}: {votes} votes ({int(round((votes/total_votes)*100, 2))}%)\n"
    # Prepare a string that contains votes summary
    results = f"\nElection Results\n---------------------------\nTotal Votes: {total_votes}\n---------------------------\n{print_candidates}\n---------------------------\n{print_winner}"
    return results


# create a master function vote_counter that performs all the sub functions above
def vote_counter(path):
    data = read_file(path)
    candidate_dict, total_votes = count_vote(data)
    results = calculate_results(candidate_dict, total_votes)
    print(results)
    with open("output_file.txt", "w") as doc:
        doc.write(results)
    
vote_counter("election_data.csv")