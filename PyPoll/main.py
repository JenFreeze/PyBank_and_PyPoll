# Import dependencies
import os
import csv

# Import csv file
csvpath = os.path.join("Resources", "election_data.csv")

# Define variables
votes = []
candidate_list = []
votes_received = []
percent_of_vote = []

# Open CSV file and skip header
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Calculate total number of votes cast
    for row in csvreader:
        votes.append((row[2]))
    votes_cast = len(votes)
        
    # Create list of candidates receiving votes
    for candidate in votes:
        if candidate not in candidate_list:
            candidate_list.append(candidate)
    
    # Calculate number of votes received by each candidate and put into a list
    for candidate in candidate_list:
        candidate_votes = votes.count(str(candidate))
        votes_received.append(candidate_votes)

    # Calculate % of vote received by each candidate and put into a list
    for votes in votes_received:
        candidate_vote_percentage = round((votes / votes_cast)*100,3)
        percent_of_vote.append(str(candidate_vote_percentage)+"%")  
    
# Create dictionary to store candidate information
candidate_dict = {"Name":candidate_list,
                "Number of Votes":votes_received,
                "Percent of Vote":percent_of_vote}

# Determine winner of election
count = 0
winner = 0
for candidates in candidate_list:
    if candidate_dict["Number of Votes"][count] > winner:
        winner = candidate_dict["Number of Votes"][count]
        winning_name = str(candidate_dict["Name"][count])
        count = count + 1

# Print results to terminal and to text file
line1 = "Election Results"
line2 = "------------------------"
line3 = "Total Votes: " + str(votes_cast)
line4 = "Winner: " + str(winning_name)

count = 0
lines = []
for candidates in candidate_list:
    line = (str(candidate_dict["Name"][count]) +": " + str(candidate_dict["Percent of Vote"][count]) + " (" + str(candidate_dict["Number of Votes"][count]) + ")")
    lines.append(line)
    count = count + 1

output_info = [line1, line2, line3, line2, lines[0], lines[1], lines[2], line2, line4, line2]

print("\n".join(output_info))
      
with open("analysis\output.txt", "w") as output:
    output.writelines("\n".join(output_info))