import os 
import csv


pypoll = os.path.join('..', 'Resources', 'election_data.csv')

def voter_challenge(voter_data):
    #assign variable to columns
    idnum = int(voter_data[0])
    county = str(voter_data[1])
    candidate = str(voter_data[2])
    
    #count the names in the column for the candidates
    Khan_votes = candidate.count('Khan')
    Correy_votes = candidate.count('Correy')
    Li_votes = candidate.count('Li')
    Tooley_votes = candidate.count("O'Tooley")
    
    #count the rows which should equal the total number of votes
    row_count = list(candidate)
    total_votes = len(row_count)
    
    #calculate the percents
    vote_percent1 = (Khan_votes / total_votes) * 100
    vote_percent2 = (Correy_votes / total_votes) * 100
    vote_percent3 = (Li_votes / total_votes) * 100
    vote_percent4 = (Tooley_votes / total_votes) * 100
    
    max_votes = max(Khan_votes, Correy_votes, Li_votes, Tooley_votes) 
    
    print('Election Results')
    print('_________________________')
    #row count = the number of row since each voter only gets one voter
    print(f'Total Voters: {total_votes}')   
    print('_________________________')
    print(f'Khan: {vote_percent1}% "({Khan_votes})"')
    print(f'Correy: {vote_percent2}% "({Correy_votes})"')
    print(f'Li: {vote_percent3}% "({Li_votes})"')
    print(f"O'Tooley: {vote_percent4}% '({Tooley_votes})'")
    print('__________________________')
    print(f'Winner: {max_votes}')
    
 #read in file       
with open(pypoll, 'r') as csvfile:
    #split the data by comma
    readcsv = csv.reader(csvfile, delimiter=",")
    
    header = next(readcsv)
    
    for row in readcsv:
        voter_challenge(row)