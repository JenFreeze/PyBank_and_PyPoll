# Import dependencies
import os
import csv

#Import csv file
csvpath = os.path.join("Resources", "election_data.csv")

ballot_id = []
county = []
candidates = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    output_cand = []

    for row in csvreader:
        ballot_id.append((row[0]))
        county.append((row[1]))
        candidates.append((row[2]))
    
    votes_cast = len(ballot_id)
    
    candidates_dictionary = {}
    candidates_dictionary = dict()
    
    for candidate in candidates:
        if candidate not in output_cand:
            output_cand.append(candidate)
    
    total_votes = []
    for cand in output_cand:
        total_votes_gotten = candidates.count(str(cand))
        total_votes.append(total_votes_gotten)

    percent_votes = []
    for votes in total_votes:
        percent_votes_gotten = round((votes / votes_cast)*100,3)
        percent_votes.append(str(percent_votes_gotten)+"%")
 
    # count = 0
    # #for x in output_cand:
    #     #candidate_dictionary = {
    #         #"name":output_cand[count],
            #"total votes":total_votes[count],
            #"percent":percent_votes[count]
        #}
        #count = count + 1
        #print(candidate_dictionary)
    
    #candidate_dictionary = {}
    #for x in output_cand:
        #candidate_dictionary[output_cand[count]] = [percent_votes[count], total_votes[count]]
        #count = count + 1
    #print(candidate_dictionary)
    

    #count = 0
    #print(candidate_dictionary[output_cand[0]][0])
    #winner = 0

    # count = 1
    # candidate_dictionary = {}
    # candidate1_dictionary = {}
    # for candidate in output_cand:
    #     candidate_dictionary[str("candidate" + str(count))] = candidate
        
    #     count = count + 1
    # print(candidate_dictionary)
    # candidate1_dictionary = {
    #     "name": output_cand[0],
    #     "votes": {
    #     "total votes": total_votes[0],
    #     "percent of vote": percent_votes[0]
    #     }
    # }
    # print(candidate1_dictionary)
    # print(str(candidate1_dictionary["name"]) + " received " + str(candidate1_dictionary["votes"]["total votes"]) + " votes")
    
summary_dict = {"Name":output_cand,
                "Number of Votes":total_votes,
                "Percent of Vote":percent_votes}
print(summary_dict)

count = 0
winner = 0
for candidates in output_cand:
    if summary_dict["Number of Votes"][count] > winner:
        winner = summary_dict["Number of Votes"][count]
        winning_name = str(summary_dict["Name"][count])
        count = count + 1

line1 = "Election Results"
line2 = "------------------------"
line3 = "Total Votes: " + str(votes_cast)
line4 = "Winner: " + str(winning_name)
print(line1)
print(line2)
print(line3)
print(line2)

count = 0
lines = []
for candidates in output_cand:
    line = (str(summary_dict["Name"][count]) +": " + str(summary_dict["Percent of Vote"][count]) + " (" + str(summary_dict["Number of Votes"][count]) + ")")
    lines.append(line)
    #print(lines)
    count = count + 1
print("\n".join(lines))


print(line2)
print(line4)
print(line2)
output_info = [line1, line2, line3, line2, lines[0], lines[1], lines[2], line2, line4, line2]

with open("output.txt", "w") as output:
    output.writelines("\n".join(output_info))