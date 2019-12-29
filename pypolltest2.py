import os 
import csv

pypoll = os.path.join('..', 'Resources', 'election_data.csv')

with open(pypoll, 'r') as csvfile:
    readcsv = csv.reader(csvfile, delimiter=",")
    next(readcsv)
    
    #creating new seperate list
    voter_id = []
    voter_county = []
    voter_candidate = []
    
    #trying to count Khans in list
    count1 = 0
    Khan_count = 'Khan'
    
           
    #to get the number of voters im reading the list after passint titles
    votercount = list(readcsv)
    row_count = len(votercount) 
    #obviously print Results
    print('Election Results')
    print('_________________________')
    #row count = the number of row since each voter only gets one voter
    print(f'Total Voters: {row_count}')   
    print('_________________________')
    #attempting to take the count of Khan votes and print
    #in theory would need to make counter for each candidate if it works
    
    print(voter_candidate)     
    
    for row in readcsv:
        idnum = row[0]
        county = row[1]
        candidate = row[2]
        
        
        voter_id.append(idnum)
        voter_county.append(county)
        voter_candidate.append(candidate)
        
        while Khan_count =='Khan' in candidate:
            count1 = count1 + 1
            print(count1)
    
                
            
            
            
              