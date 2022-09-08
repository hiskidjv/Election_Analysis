#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who receieved votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular votes
import os
import csv
election_stuff='Resources/election_results.csv'
#Open the election results and read the file
with open(election_stuff) as election_data:

    #To do: read and analyze data here

    #This references the object
    file_reader = csv.reader(election_data)
    #Print just the header row- next tells it to be skipped.
    headers=next(file_reader)    
    print(headers)




