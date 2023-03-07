import os
import csv

# create a path for both csv file i'll read and txt file i'll write to
csv_path = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join("analysis", "PyBank.txt")

# empty lists declared to be filled later with csv data
months = []
profits = []
profit_change = []

# open file, append months and profits to list, find min and max profits
with open(csv_path, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    
    for row in csv_reader:
       months.append(row[0])
       profits.append(int(row[1]))
    
    for cash in range(len(profits) - 1):
        profit_change.append(int(profits[cash+1]) - int(profits[cash]))
    
    max_profits = max(profit_change)
    max_month = profit_change.index(max(profit_change)) + 1
    min_profits = min(profit_change)
    min_month = profit_change.index(min(profit_change)) + 1
    
    # print analysis to terminal window
    print("Financial Analysis")
    print("---------------------------")
    print(f"Total Months: {len(months)}")
    print(f"Total: ${sum(profits)}")
    print(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
    print(f"Greatest Increase In Profits: {months[max_month]} (${max_profits})")
    print(f"Greatest Decrease In Profits: {months[min_month]} (${min_profits})")
    
    # write same data to a .txt file and place in analysis folder
    with open(output_path, "w") as txt_file:
        txt_file.write("Financial Analysis\n")
        txt_file.write("---------------------------\n")
        txt_file.write(f"Total Months: {len(months)}\n")
        txt_file.write(f"Total: ${sum(profits)}\n")
        txt_file.write(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}\n")
        txt_file.write(f"Greatest Increase In Profits: {months[max_month]} (${max_profits})\n")
        txt_file.write(f"Greatest Decreasse In Profits: {months[min_month]} (${min_profits})\n")
        
