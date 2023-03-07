import os
import csv

csv_path = os.path.join("Resources", "budget_data.csv")

months = []
profits = []
profit_change = []

with open(csv_path) as csv_file:
        
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
    
    print("Financial Analysis")
    print("---------------------------")
    print(f"Total Months: {len(months)}")
    print(f"Total: ${sum(profits)}")
    print(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
    print(f"Greatest Increase In Profits: {months[max_month]} (${max_profits})")
    print(f"Greatest Decrease In Profits: {months[min_month]} (${min_profits})")
    
