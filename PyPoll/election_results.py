#import libraries
import os
import csv

#file path 
dataPath = os.path.join("Resources", "election_data.csv")

#create variables
totalVotes = 0 #count of total votes cast
candidates = {} #dictionary candidates

#open the file using "read" mode 
with open(dataPath, 'r', encoding='utf') as csvfile:
    pollData = csv.reader(csvfile, delimiter=",") 
    next(pollData) #skip the header
    for i in pollData: 
        if i[2] not in candidates: #check if candidate voted for is in dictionary if not:
            candidates[str(i[2])] = [1, 0] #add  = candidate name and values = vote count and percentage of votes
        else: #if candidate is in dictionary  add a vote to their tally
            candidates[str(i[2])][0] += 1
        totalVotes += 1 
    for i in candidates: 
        candidates[f'{i}'][1] = candidates[f'{i}'][0]/totalVotes


#print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------")
for i in candidates:
    print(f"{i}: {round(candidates[f'{i}'][1]*100,3)}% ({candidates[f'{i}'][1]})")
print("-------------------------")

#compare to see the winner
winner = 0
for i in candidates:
    if candidates[f'{i}'][0] > winner:
        chickenDinner = i
        winner = candidates[f'{i}'][0]
print(f"Winner: {chickenDinner}")
print("-------------------------")

#write to a text file
with open("analysis\election_results.txt", 'w') as file:
    print("Election Results", file=file)
    print("-------------------------", file=file)
    print(f"Total Votes: {totalVotes}", file=file)
    print("-------------------------", file=file)
    for i in candidates:
        print(f"{i}: {round(candidates[f'{i}'][1]*100,3)}% ({candidates[f'{i}'][1]})", file=file)
    print("-------------------------", file=file)
    print(f"Winner: {chickenDinner}", file=file)
    print("-------------------------", file=file)

