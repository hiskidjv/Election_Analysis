#Add dependencies
import csv
import os

#Assign variable to load file from path
election_stuff='Resources/election_results.csv'

#Assign variable to save file to path
analysis_results=os.path.join("analysis","election_analysis.txt")

#Initialize accumulator
total_votes=0

#Setting up list of names and dictionary of names to votes
candidate_options =[]
candidate_votes= {}

# Winning Candidate and Winning Count Trackers
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the object for the file and read the file
with open(election_stuff) as election_data:
    file_reader = csv.reader(election_data)
   
    #read header row
    headers=next(file_reader)  
   
    #go through each row to get info
    for row in file_reader:

        #increase accumulator
        total_votes += 1

        #put names into variable             
        candidate_name= row[2]

        #put variable into list uniquely
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #begin tracking vote counts
            candidate_votes[candidate_name]=0

        #Add a vote to that candidate's count (out of conditional and still under loop)
        candidate_votes[candidate_name]+=1

# Save the results to our text file.
with open(analysis_results, "w") as txt_file:
    
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    for candidate_name in candidate_votes:

        # Retrieve vote count of a candidate and calculate percentage
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, percentage, and name
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    #Print out the winner in terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)

