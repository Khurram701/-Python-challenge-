
import csv
with open('C:/Users/Khurram/Desktop/GitHub Repos/election_data.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    total_votes = 0
    for x in reader:
        total_votes+= 1
    print(total_votes)

with open ('C:/Users/Khurram/Desktop/GitHub Repos/test.txt','w') as text_file:
    text_file.write('total_votes')






import csv
with open('C:/Users/Khurram/Desktop/GitHub Repos/election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) # skip the header row
    vote_count = {}
    total_votes = 0
    for row in csvreader:
        candidate = row[2]
        if candidate not in vote_count:
            vote_count[candidate] = 1
        else:
            vote_count[candidate] += 1
        total_votes += 1
    for candidate, votes in vote_count.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.1f}% ({votes})")


with open ('C:/Users/Khurram/Desktop/GitHub Repos/test.txt','w') as text_file:
    text_file.write(('Percentage' , 'Votes'))






import csv
with open('C:/Users/Khurram/Desktop/GitHub Repos/election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) # skip the header row
    vote_count = {}
    total_votes = 0
    for row in csvreader:
        candidate = row[2]
        if candidate not in vote_count:
            vote_count[candidate] = 1
        else:
            vote_count[candidate] += 1
        total_votes += 1
    winning_candidate = ""
    winning_votes = 0
    for candidate, votes in vote_count.items():
        if votes > winning_votes:
            winning_candidate = candidate
            winning_votes = votes
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.1f}% ({votes})")
    print(f"The winner of the election is {winning_candidate} with {winning_votes} votes.")


    
with open ('C:/Users/Khurram/Desktop/GitHub Repos/test.txt','w') as text_file:
    text_file.write(('Winning_candidate' , 'Winning_Votes'))
