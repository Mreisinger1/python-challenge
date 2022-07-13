#import os module
import os
#module for reading csv files
import csv

#file path
csvpath= os.path.join("Resources","election_data.csv")

#define variables
count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []
a = []
b = []
c = []
winning_vote_count = []
winner = []

#open csv path
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
#for loop to find all data 
    for row in csvreader:
       count = count + 1
       candidatelist.append(row[2])
#make a list of candidates
    for a in set(candidatelist):
        unique_candidate.append(a)
#list of vote counts per candidate
        b = candidatelist.count(a)
        vote_count.append(b)
#list of vote percentages per candidate
        c = (b/count)*100
        vote_percent.append(c)

    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]

#print results to terminal 
print("Election Results")
print("Total Votes:" + str(count))
print("Candidates:" + "Charles Casper Stockham, Diana DeGette, Raymon Anthony Doane")
print("Winner:" + (winner) + " " + "with" + " " + str(winning_vote_count) + " " + "votes")

#print results to a text file
with open ('election_data.txt', 'w') as text:
    text.write("Election Results"+ "\n")
    text.write("Total Votes:" + str(count) + '\n')
    text.write("Candidates:" + "Charles Casper Stockham, Diana DeGette, Raymon Anthony Doane" + "\n") 
    text.write("Winner:" + (winner) + " " + "with" + " " + str(winning_vote_count) + " " + "votes" + "\n")



