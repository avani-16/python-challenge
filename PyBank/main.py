import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')
#print(budget_csv)

total_month = 0
net_profit_loss = 0
data_list = []
total_monthly_change = 0
greatest_increase = 0
greatest_decrease = 0

with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile , delimiter = ',')
    header = next(csvreader)
   # print(header)
    for row in csvreader:
      date = row[0]
      #print(date)
      total_month = total_month + 1
#print(total_month)
      net_profit_loss += int(row[1])
#print(net_profit_loss)
      
    # put data into a list to calculate monthly change
      data_list.append(row)

    # The net total amount of "Profit/Losses" over the entire period
    for i in range(len(data_list)-1):
       #print(i)
       monthly_change = int(data_list[i+1][1]) - int(data_list[i][1])
       #print(monthly_change)

    # Average of these changes
       total_monthly_change += round((monthly_change),2)
       avg_monthly_change = round(total_monthly_change/(total_month-1),2)
#print(avg_monthly_change)
    
    # Greatest increase in profit
       if monthly_change > greatest_increase:
          greatest_increase = monthly_change
          increase_month = data_list[i+1][0]
#print(greatest_increase)
    
    # Greatest decrease in profit
       if monthly_change < greatest_decrease:
          greatest_decrease = monthly_change
          decrease_month = data_list[i+1][0]
#print(greatest_decrease)
  
# Export a text file with results (Created "analysis" folder and sent text file there)
with open('analysis/Financial_analysis.txt','w') as f:
    f.write("Financial Analysis.\n\n")
    f.write("--------------------------\n\n")
    f.write(f"Total months: {total_month}\n") 
    f.write(f"Total: ${net_profit_loss}\n") 
    f.write(f"Average Change: ${avg_monthly_change}\n")  
    f.write(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})\n")
    f.write(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})\n")

# Print Financial Analysis output in terminal
print("\nFinancial Analysis\n")
print("--------------------------\n")
print(f"Total months: {total_month}\n") 
print(f"Total: ${net_profit_loss}\n") 
print(f"Average Change: ${avg_monthly_change}\n")  
print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})\n")
print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})\n")