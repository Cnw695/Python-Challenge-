import os
import csv

pypoll = os.path.join('..', 'Resources', 'election_data.csv')

#opening the file 
with open (pypoll, 'r') as csvfile:
    readcsv = csv.reader(csvfile, delimiter=',')
    header = next(readcsv) 
    #obviously print header
    print(header)
    
    #so many variables
    total_count = 0
    candidates = []
    vote_summary = {}
    percent = {}
    Winner = 0
    winning_candidate = ""
    #the easiest way i could think to use the name due to the '
    name = "O'Tooley"
    #read that thang
    for row in readcsv:
        #simple count of rows after header
        total_count += 1
        #if the candidate name is not in the list then put it in 
        if row[2] not in candidates:
            candidates.append(row[2])
            #once the name is there make a dictionary and begin adding 
            vote_summary[row[2]] = 0
        vote_summary[row[2]] = vote_summary[row[2]] + 1
        #i was name until i changed it 
        #.get might be life changing but i still dont full understand it 
    for i in vote_summary:
        votes = vote_summary.get(i)
        percent[i] = (votes / total_count) * 100
        if votes > Winner:
            Winner = votes
            winning_candidate = i
            
      
    print(f"Election Results")
    print('_____________________________')
    print(f'Total Votes: {total_count}')
    print('_____________________________')
    print(f"Khan: {percent['Khan']:.3f}% ({vote_summary['Khan']})")
    print(f"Correy: {percent['Correy']:.3f}% ({vote_summary['Correy']})")
    print(f"Li: {percent['Li']:.3f}% ({vote_summary['Li']})") 
    print(f"O'Tooley: {percent[name]:.3f}% ({vote_summary[name]})") 
    print('_____________________________')
    print(f'Winner: {winning_candidate}')
    print('_____________________________')
    
    
output_path = os.path.join("..", "PyPoll_results.txt")

with open(output_path, 'w') as txtfile:
    txtwriter = csv.writer(txtfile, delimiter=',')
    

    txtwriter.writerow([f"Election Results"]),
    txtwriter.writerow(['_____________________________']),
    txtwriter.writerow([f'Total Votes: {total_count}']),
    txtwriter.writerow(['____________________________']),
    txtwriter.writerow([f"Khan: {percent['Khan']:.3f}% ({vote_summary['Khan']})"]),
    txtwriter.writerow([f"Correy: {percent['Correy']:.3f}% ({vote_summary['Correy']})"]),
    txtwriter.writerow([f"Li: {percent['Li']:.3f}% ({vote_summary['Li']})"]), 
    txtwriter.writerow([f"O'Tooley: {percent[name]:.3f}% ({vote_summary[name]})"]), 
    txtwriter.writerow(['_____________________________']),
    txtwriter.writerow([f'Winner: {winning_candidate}']),
    txtwriter.writerow(['_____________________________'])