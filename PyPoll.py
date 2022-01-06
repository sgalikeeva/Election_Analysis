#Data needed
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

#Add our dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Assign variable for total votes
total_votes=0

# Declare candidate options list
candidate_options=[]

# Declare candidate votes dictionary
candidate_votes={}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row in the CSV file.
    headers = next(file_reader)

    # Print each row in file
    for row in file_reader:
        # Add to total vote count
        total_votes+=1
        # Print candidate names from each row
        candidate_name=row[2]
        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add to list of candidates 
            candidate_options.append(candidate_name)
            # Create each candidate as key and track each candidate's vote
            candidate_votes[candidate_name] = 0
        # Add a count to candidate each time appears in row
        candidate_votes[candidate_name] += 1

# Use the open statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Print final vote count and save to text file
    election_results = (
        f"\nElection Results\n"
        f"----------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------\n")
    print(election_results,end="")
    txt_file.write(election_results)

    # Determine percentage of votes for each candidate
    # Iterate through candidate list
    for candidate_name in candidate_votes:
        # Retrieve votes of candidate
        votes=candidate_votes[candidate_name]
        # Calculate percentage
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print out each candidate's name, vote count, and percentage of votes to the terminal and text file
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine the winning candidate by the number and percentage of votes.   
        # Determine if the vote count that was calculated is greater than the winning_count.
        if (votes > winning_count) and (vote_percentage> winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent = # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    # Print winning candidate, vote count and percentage
    winning_candidate_summary = (
        f"--------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)