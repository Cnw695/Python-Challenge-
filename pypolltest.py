import os 
import csv

pypoll = os.path.join('..', 'Resources', 'election_data.csv')

#function struggles
def voter_percentages(voterdata):
    totalvotes = int(voterdata[0])
    allcandidates = str(voterdata[2])
    
    #precent_votes = 
    



with open(pypoll, 'r') as csvfile:
    readcsv = csv.reader(csvfile, delimiter=",")
    next(readcsv)
    
    voter_id = []
    voter_county = []
    voter_candidate = []
    
    
    
    for row in readcsv:
        idnum = row[0]
        county = row[1]
        candidate = row[2]
        
        voter_id.append(idnum)
        voter_county.append(county)
        voter_candidate.append(candidate)
        
        for name in voter_candidate:
            if name == "Khan":
                print(str('Khan'))
            
            
        
    
        
        
        
        