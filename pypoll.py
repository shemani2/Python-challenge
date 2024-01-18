#import files
import csv

#Read csv file
with open('election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    
    #variables
    votes = list(csvreader)
    total_votes = len(votes) - 1
    candidates = {}

    for row in votes[1:]:
        if row[2] not in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1
       
#Store results
results = []

#run for loop
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, votes, percentage))

#candidate with most votes
winner = max(candidates, key=candidates.get)
print(f"Winner: {winner}")

#total vote result
print(f"Total Votes: {total_votes}")

#print results
print("Election Results")
print("----------------------------------------")
print(f"Total Votes: {total_votes}")

for candidate, votes, percentage in results:
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("----------------------------------------")
print(f"Winner: {winner}")

# Define the output file path
output_file = "election_results.txt"

# Open the file and write the results to it
with open(output_file, "w") as file:
    file.write("Election Results\n")
    file.write("-" * 40 + "\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-" * 40 + "\n")

    for candidate, votes, percentage in results:
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    file.write("-" * 40 + "\n")
    file.write(f"Winner: {winner}\n")
    file.write("-" * 40 + "\n")


