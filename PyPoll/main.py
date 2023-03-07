import os
import csv

# create a path for both csv file i'll read and txt file i'll write to
csv_path = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("analysis", "PyPoll.txt")

# declared variables set to tally votes
votes = 0
stockham = 0
degette = 0
doane = 0

# open file, tally votes and find winner
with open(csv_path, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    
    for row in csv_reader:
        votes += 1
        if row[2] == "Charles Casper Stockham":
            stockham += 1
        elif row[2] == "Diana DeGette":
            degette += 1
        else:
            doane += 1
    
    if degette > stockham and degette > doane:
        winner = "Diana DeGette"
    elif stockham > degette and stockham > doane:
        winner = "Charles Casper Stockham"
    else:
        winner = "Raymon Anthony Doane"
    
    
    # print analysis to terminal window
    print("Election Results")
    print("---------------------------")
    print(f"Total Votes: {votes}")
    print("---------------------------")
    print(f"Charles Casper Stockham: {round((stockham/votes*100), 3)}% ({stockham})")
    print(f"Diana DeGette: {round((degette/votes*100), 3)}% ({degette})")
    print(f"Raymon Anthony Doane: {round((doane/votes*100), 3)}% ({doane})")
    print("---------------------------")
    print(f"Winner: {winner}")
    print("---------------------------")
    
    # write same data to a .txt file and place in analysis folder
    with open(output_path, "w") as txt_file:
        txt_file.write("Election Results\n")
        txt_file.write("--------------------------\n")
        txt_file.write(f"Total Votes: {votes}\n")
        txt_file.write("--------------------------\n")
        txt_file.write(f"Charles Casper Stocham: {round((stockham/votes*100), 3)}% ({stockham})\n")
        txt_file.write(f"Diana DeGette: {round((degette/votes*100), 3)}% ({degette})\n")
        txt_file.write(f"Raymon Anthony Doane: {round((doane/votes*100), 3)}% ({doane})\n")
        txt_file.write("--------------------------\n")
        txt_file.write(f"Winner: {winner}\n")
        txt_file.write("--------------------------")