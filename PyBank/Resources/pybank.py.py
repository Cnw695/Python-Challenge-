import os
import csv

# Path to collect data from the Resources folder
pybank = os.path.join('..', 'Resources', 'budget_data.csv')

total_count = 0
change_list = []
previous = 0
total = 0
max_profit_loss = 0
bank_info = {}
date = []


with open(pybank, 'r') as csvfile:
    readcsv = csv.reader(csvfile, delimiter=',')
    header = next(readcsv) 
    #obviously print header
    print(header)                        
                        
    for row in readcsv:
        #count rows
        total_count += 1
        # dollar total is the total + next value added to total and commenced
        total = total + int(row[1])
        #change either postive or negative will be the current - previous
        #doesnt work if you put the previous calcuation first 
        change = int(row[1]) - previous
        previous = int(row[1])
       #store changes in a list
        change_list = change_list + [change]
        date.append(row[0])
    
    count = 0
    for c in range(len(change_list)):
                            
        if c == 0:
            highest = change_list[c]
            hDate = date[c]
            lowest = change_list[c]
            lDate = date[c]
        else:
            if change_list[c] > highest:
                                    highest = change_list[c]
                                    hDate = date[c]
                                    
            if change_list[c] < highest:
                                    lowest = change_list[c]
                                    lDate= date[c]                                                                                                
                                
    average = sum(change_list[1:]) / len(change_list[1:])
    
    print(f'Financial Analysis')
    print('___________________________')
    print(f'Total Months: {total_count}')
    print(f'Total: ${total}')
    print(f'Average Change: ${average:.2f}')
    print(f'Greatest Increse in Profits: {hDate} (${max(change_list)})')
    print(f'Greatest Decrease in Profits: {lDate} (${min(change_list)})')
    #print(f'Greatest Month Increse in Profits: {hDate}')
   # print(f'Greatest Month Decrease in Profits: {lDate}')  
    
output_path = os.path.join("..", "PyBank_results.txt")

with open(output_path, 'w') as txtfile:
    txtwriter = csv.writer(txtfile, delimiter=',')
    
    txtwriter.writerow([f'Financial Analysis'])
    txtwriter.writerow(['___________________________'])
    txtwriter.writerow([f'Total Months: {total_count}'])
    txtwriter.writerow([f'Total: ${total}'])
    txtwriter.writerow([f'Average Change: ${average:.2f}'])
    txtwriter.writerow([f'Greatest Increse in Profits: {hDate} (${max(change_list)})'])
    txtwriter.writerow([f'Greatest Decrease in Profits: {lDate} (${min(change_list)})'])    

    
 
    
    
    




