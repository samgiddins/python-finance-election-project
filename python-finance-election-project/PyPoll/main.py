#as always...
import os
import csv 

#Read in CSV and open w/ proper headers
csvpath = os.path.join("/Users/samuelgiddins/desktop/PythonChallenge/PyPoll/election_data.csv")
with open(csvpath, newline='') as pypoll:
    #set starting values and blank lists to store everything
    election_data = csv.reader(pypoll, delimiter=',')
    csv_header = next(election_data)

    
#set starting values and blank lists
    candidate_list = []
    vote_count = 0
    candidate_1_count = 0
    candidate_2_count = 0
    candidate_3_count = 0
    candidate_4_count = 0
    winner = ""

# Count total number of votes
    for row in election_data:
        vote_count += 1
        candidate_list.append(row[2])    
    
    # create a set for unique candidates
    candidate_set = set(candidate_list)
#print(set(candidate_list)) so we know all the candidates we will be looking at later
    
    #create a list to store every occurrence each candidate comes up (we will use this to count votes for each candidate later)
    candidate_1_list = []
    candidate_2_list = []
    candidate_3_list = []
    candidate_4_list = []
    
    #add occurrences for each candidate to their respective list
    for x in candidate_list:
        if x == "Correy":
            candidate_1_list.append(x[0])
        elif x == "Li":
            candidate_2_list.append(x[0])
        elif x == "Khan":
            candidate_3_list.append(x[0])
        elif x == "O'Tooley":
            candidate_4_list.append(x[0])
    
#count the number of votes for each candidate by looping through their occurrence lists
    for i in range(len(candidate_1_list)):
        candidate_1_count += 1
      
    for i in range(len(candidate_2_list)):
        candidate_2_count += 1
        
    for i in range(len(candidate_3_list)):
        candidate_3_count += 1
        
    for i in range(len(candidate_4_list)):
        candidate_4_count += 1
    
    #calculate percentage of total votes for each candidate
    correy_pct = candidate_1_count/vote_count
    li_pct = candidate_2_count/vote_count
    khan_pct = candidate_3_count/vote_count
    otooley_pct = candidate_4_count/vote_count
    
#clunky conditionals to declare a winner    
    if candidate_1_count > candidate_2_count and candidate_1_count > candidate_3_count and candidate_1_count > candidate_4_count:
        winner = "Correy"
    elif candidate_2_count > candidate_1_count and candidate_2_count > candidate_3_count and candidate_2_count > candidate_4_count:
        winner = "Li"
    elif candidate_3_count > candidate_1_count and candidate_3_count > candidate_2_count and candidate_3_count > candidate_4_count:
        winner = "Khan"
    elif candidate_4_count > candidate_1_count and candidate_4_count > candidate_2_count and candidate_4_count > candidate_3_count:
        winner = "O'Tooley"
        
    
#print results to the terminal
print("Election Results") 
print("-------------------------") 
print("Total Votes: " + str(vote_count))
print("-------------------------") 
print("Correy: " + str(round(correy_pct*100,2)) + "%" + " (" + str(candidate_1_count) + ")")
print("Li: " + str(round(li_pct*100, 2)) + "%" + " (" + str(candidate_2_count) + ")")
print("Khan: " + str(round(khan_pct*100, 2)) + "%" + " (" + str(candidate_3_count) + ")")
print("O'Tooley: " + str(round(otooley_pct*100, 2)) + "%" + " (" + str(candidate_4_count) + ")")
print("-------------------------") 
print("Winner: " + winner)


#write these results to a new text file
file = open("/users/samuelgiddins/desktop/pythonchallenge/pypoll/pypoll.txt", 'w') 
 
file.write("Election Results\n")
file.write("----------------------\n") 
file.write("Total Votes: " + str (vote_count) + "\n") 
file.write("----------------------\n")
file.write("Correy: " + str(round(correy_pct*100,2)) + "%" + " (" + str(candidate_1_count) + ")\n") 
file.write("Li: " + str(round(li_pct*100, 2)) + "%" + " (" + str(candidate_2_count) + ")\n")
file.write("Khan: " + str(round(khan_pct*100, 2)) + "%" + " (" + str(candidate_3_count) + ")\n")
file.write("O'Tooley: " + str(round(otooley_pct*100, 2)) + "%" + " (" + str(candidate_4_count) + ")\n")
file.write("----------------------\n")
file.write("Winner " + winner + "\n") 

file.close() 