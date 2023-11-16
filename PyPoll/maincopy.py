import os
import csv

election_csv = os.path.join('Resources','election_data.csv')

total_vote = 0
candidate_count = 0 
candidate_list = []
count = 0
count_list = {}
winner = 0

with open(election_csv, encoding = 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    #print(header)
    print(csvreader)

    for row in csvreader:
        total_vote = total_vote + 1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            count_list[row[2]] = 0
       
        count_list[row[2]] += 1

        #for i in candidate_list:
             #print(i)

                #if i == row[2]:
                    #count +=1
                #count_list[i] = count
                #count_list[row[2]] = 0

                #count_list[row[2]] = 0
        #count_list[row[2]] += 1
        # The total number of votes cast 
        winner = 0
    for key,value in count_list.items():
        percent = round((value/total_vote)*100,3)
        #print(key, percent, (value))
    
        winner = max(count_list.values())
        winner_name = max(count_list, key = count_list.get)
         
    print(winner)
    print(winner_name)
    #print(total_vote)
    #print(count_list)


