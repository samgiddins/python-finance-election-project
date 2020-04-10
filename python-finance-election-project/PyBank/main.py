#as always...
import os
import csv 

#define monthly_change function
def monthly_change(next_month, current_month):
    net_prof_month = next_month-current_month
    return net_prof_month

    
#Read in CSV and open w/ proper headers
csvpath = os.path.join("/Users/samuelgiddins/desktop/PythonChallenge/PyBank/budget_data.csv")
with open(csvpath, newline='') as pybank:
    #set starting values and blank lists to store everything
    budget_data = csv.reader(pybank, delimiter=',')
    csv_header = next(budget_data)
    monthly_profit = []
    month_list = []
    total_profit = 0
    month_count = 0
    running_change = 0
    
    #store the months and their corresponding profits each into lists    
    for row in budget_data:
        month_list.append(row[0])
        monthly_profit.append(int(row[1]))
        total_profit += int(row[1])
        month_count += 1
    
    
    #calculate the running change in monthly profit and divide it by the length of the list to get average change
    for x in range(0, len(monthly_profit)-1):
        running_change += (monthly_change(monthly_profit[x+1], monthly_profit[x]))
    average_change = running_change/len(monthly_profit)-1
    

    #store each month's change in profit in a list
    monthly_net_change = []
    for x in range(0, len(monthly_profit)-1):
        monthly_net_change.append(monthly_profit[x+1] - monthly_profit[x])
    max_change = max(monthly_net_change)            
    min_change = min(monthly_net_change)   
 

    #find the index for the month where the greatest increase occured
    max_month_index = 0
    max_change_index = monthly_net_change[0]
    for i in range(len(monthly_net_change)):
        if monthly_net_change[i] > max_change_index:
            max_month_index = i
            max_change_index = monthly_net_change[i]
    
    
    #find the index for the month where the greatest decrease occurred
    min_month_index = 0
    min_change_index = monthly_net_change[0]
    for i in range(len(monthly_net_change)):
        if monthly_net_change[i] < min_change_index:
            min_month_index = i
            min_change_index = monthly_net_change[i]
  
#print the final summary to the terminal
print("Financial Analysis")
print("----------------------")
print("Total Months: " + str(month_count))
print("Total: $" + str(total_profit))
print("Average Change: $" + str(round(average_change, 2)))
print("Greatest Increase in Profits: " + month_list[max_month_index + 1] + " ($" + str(max_change) + ")")
print("Greatest Decrease in Profits: " + month_list[min_month_index + 1] + " ($" + str(min_change) + ")")


#write these results to a new text file
file = open("/users/samuelgiddins/desktop/pythonchallenge/pybank/pybank.txt", 'w') 
 
file.write("Financial Analysis\n")
file.write("----------------------\n") 
file.write("Total Months: " + str(month_count) + "\n") 
file.write("Total: $" + str(total_profit) + "\n") 
file.write("Average Change: $" + str(round(average_change, 2)) + "\n")
file.write("Greatest Increase in Profits: " + month_list[max_month_index + 1] + " ($" + str(max_change) + ")\n")
file.write("Greatest Decrease in Profits: " + month_list[min_month_index + 1] + " ($" + str(min_change) + ")\n")
 
file.close() 




