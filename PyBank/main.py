import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')
#print(budget_csv)

with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile , delimiter = ',')
    header = next(csvreader)
   # print(header
 total = 0 
