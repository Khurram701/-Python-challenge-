
# Total Votes
import csv

# Read the CSV file and count the total number of votes
with open('./election_data.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    total_votes = 0
    for x in reader:
        total_votes+= 1
    print(f"Total votes: {total_votes}")
       

# Calculate each candidate's total votes and percentage of votes
with open('./election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) # skip the header row
    vote_count = {}
    for row in csvreader:
        candidate = row[2]
        if candidate not in vote_count:
            vote_count[candidate] = 1
        else:
            vote_count[candidate] += 1
    results = ""
    for candidate, votes in vote_count.items():
        percentage = (votes / total_votes) * 100
        results += f"{candidate}: {percentage:.1f}% ({votes})\n"
    winning_candidate = max(vote_count, key=vote_count.get)
    results += f"The winner of the election is {winning_candidate} with {vote_count[winning_candidate]} votes."
    print(results)
# Write the results to a text file
with open('ELECTION DATA.txt', 'w') as text_file:
    text_file.write(f"Total Votes:{total_votes}\n{results}")
