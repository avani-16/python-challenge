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
    

    for row in csvreader:
        # The total number of votes cast
        total_vote += 1
        #print(total_vote)
               
        # Find total candidate's names who received votes
        if row[2] not in candidate_list:
            candidate_list.append(row[2])

            # Find all candidate name and their votes in dictionary
            count_list[row[2]] = 0
        count_list[row[2]] += 1
#print(count_list)
  
    # Print Total votes in terminal
    print(f"Election Results")
    print("----------------------")
    print(f"Total Votes: {total_vote}")
    print("----------------------")
    
    # Print Total Votes in text file (Created "Analysis" folder and sent file there )
    with open('analysis/Election_result.txt','w') as f:
        f.write("Election Results\n\n")
        f.write("--------------------------\n\n")
        f.write(f"Total Votes: {total_vote}\n\n") 
        f.write("--------------------------\n\n")
        #f.close()

        # Find percentage of votes each candidate won
        for key,value in count_list.items():
            percent = round((value/total_vote)*100,3)
            # Print percentage of vote and total vote for each candidate
            print(f"{key}: {percent}% ({value})")
                    
        # Find the winner of election based on popular vote
            winner = max(count_list.values())
            winner_name = max(count_list, key = count_list.get)
            f.write(f"{key}: {percent}% ({value})\n")

       
    # Print winner name in text file
        f.write("--------------------------\n\n")
        f.write(f"Winner: {winner_name}\n\n")
        f.write("--------------------------\n\n")

    # Print winner name in terminal
    print("------------------------")
    print(f"Winner: {winner_name}")
    print("------------------------")
    
          

   
    
    
    
    
    