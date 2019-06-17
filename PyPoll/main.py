#PyPoll
# Created By Sarath K - 2019.06.13

# file is election_data.csv

import os
import csv
from collections import Counter
votes=0
win=0
i = 0
mydict={}
candidate_count=[]
vote_count=[]

# Read budget.csv file
election_csv = 'election_data.csv'

with open(election_csv, 'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    header=next(csvreader)

# count all total votes and create dictionary with poll data
    for row in csvreader:
    # Counts total voters
        votes += 1
        mydict[i]={"VoterID":row[0],"County":row[1],"Candidate":row[2]}
        i +=1
# Create count of how many votes each candidate received
        candidate=row[2]
        if candidate in candidate_count:
            candidate_index=candidate_count.index(candidate)
            vote_count[candidate_index]=vote_count[candidate_index]+1
        else:
            candidate_count.append(candidate)
            vote_count.append(1)
        

print("\nElection Results")
print("----------------------")
print(f"Total Votes: {votes}")
print("----------------------")
for i in range(len(candidate_count)):
    print(f"{candidate_count[i]}: {int(vote_count[i]*100/votes)}% ({vote_count[i]})")
# Find which candidate won the election
    if vote_count[i] > vote_count[i-1]:
        win = vote_count[i]
        name= candidate_count[i]
print("----------------------")
print(f"Winner: {name}")
print("----------------------")


