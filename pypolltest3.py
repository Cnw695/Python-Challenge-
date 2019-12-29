import os 
import csv

pypoll = os.path.join('..', 'Resources', 'election_data.csv')

#function struggles
def voter_stats(voterdata):
    totalvotes = int(voterdata[0])
    allcandidates = str(voterdata[2])
    
    
    voter_id = []
    voter_county = []
    voter_candidate = []    
    
    Khan = 1
    
    
        
        #to get the number of voters im reading the list after passint titles
    votercount = list(readcsv)
    row_count = len(votercount) 
    #obviously print Results
    print('Election Results')
    print('_________________________')
    #row count = the number of row since each voter only gets one voter
    print(f'Total Voters: {row_count}')   
    print('_________________________')
      
       
    
    for row in readcsv:
        idnum = row[0]
        county = row[1]
        candidate = row[2]
        
        voter_id.append(idnum)
        voter_county.append(county)
        voter_candidate.append(candidate)  
        
print(voter_stats)
            
        
        
with open(pypoll, 'r') as csvfile:
    readcsv = csv.reader(csvfile, delimiter=",")
    next(readcsv)    