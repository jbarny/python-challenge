import os
import csv

# locate file
os.chdir(os.path.dirname(os.path.abspath(__file__)))
election_csv = os.path.join(".", "Resources", "election_data.csv")

# initialize list
candidate_list = []

# add row index 2 to candidate list
with open(election_csv, "r", newline="") as csvfile:
    # separate data with comments
    csvreader = csv.reader(csvfile, delimiter=",")
    # skip header
    header = next(csvreader)
    for row in csvreader:
        candidate_list.append(row[2])

# calculate total number of votes cast
total_votes = len(candidate_list)
# complete list of candidates; create unique item list
candidate = []
for i in candidate_list:
    if i not in candidate:
        candidate.append(i)
# print(candidate) reveals 4 candidates, indexed 0-3
# total votes each candidate won
# khan = candidate[0]
votes0 = candidate_list.count(candidate[0])
# correy = candidate[1]
votes1 = candidate_list.count(candidate[1])
# li = candidate[2]
votes2 = candidate_list.count(candidate[2])
# otooley = candidate[3]
votes3 = candidate_list.count(candidate[3])
# percentage votes each candidate won
perc0 = votes0/total_votes * 100
perc1 = votes1/total_votes * 100
perc2 = votes2/total_votes * 100
perc3 = votes3/total_votes * 100
# winner based on popular vote
results = [perc0, perc1, perc2, perc3]
winner_perc = max(results)
winner_index = int(results.index(winner_perc))
winner = candidate[winner_index]

results = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
    f"{candidate[0]}: {perc0:.3f}% ({votes0})\n"
    f"{candidate[1]}: {perc1:.3f}% ({votes1})\n"
    f"{candidate[2]}: {perc2:.3f}% ({votes2})\n"
    f"{candidate[3]}: {perc3:.3f}% ({votes3})\n"
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------"
    )

print(results)

# specify output text file
poll_txt = os.path.join(".", "poll_data.txt")

# create .txt file
with open(poll_txt, "w") as txt:
    txt.write(results)