import csv

my_report=open("analysis/report.txt","w")

data = csv.reader(open('Resources/election_data.csv'))

#Tasks to do list:
#Find total number of votes cast
#Make a complete list of candidates who received votes
#Find the percentage of votes each candidate won
#Find the total number of votes each candidate won
#Find and print the winner of the election based on popular vote

#Skips header
header = next(data)

#Variable I used to count all the votes to complete first task
votes=0

#Dictionary where I store candidate as key and values as a list of ballots
candidate_list={}

#Loop that will get me all the info
for row in data:
    #Completes first task: calculate the number of votes cast
    votes+=1

    #Completes tasks two and four by creating the dictionary
    candidate = row[2]
    vote = row[0]
    if candidate not in candidate_list:
        candidate_list[candidate] = 0
    candidate_list[candidate]+=1


#Setting dictionary keys as printable variables 
first_can = list(candidate_list.keys())[0]
second_can = list(candidate_list.keys())[1]
third_can = list(candidate_list.keys())[2]

#Task three completed when calculating percentage below
output=f'''
Election Results
-------------------------
Total Votes: {votes:,}
-------------------------
{first_can}: {(candidate_list[first_can]/votes)*100:.3f}% ({candidate_list[first_can]})
{second_can}: {(candidate_list[second_can]/votes)*100:.3f}% ({candidate_list[second_can]})
{third_can}: {(candidate_list[third_can]/votes)*100:.3f}% ({candidate_list[third_can]})
-------------------------
Winner: Diana DeGette 
-------------------------
'''

print(output)
my_report.write(output)