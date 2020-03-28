import os 
import csv

file = os.path.join("budget_data.csv")

# declare (optional for python) and set variable equals to 0 for start
total_months = 0
total_profit = 0
greatest_inc = 0
greatest_inc_month = ""
greatest_dec = 0
greatest_dec_month = ""

previous_profit_loss = 0
changes = []

# Read csv file
with open(file) as data:
    csvreader = csv.reader(data,delimiter=",")

    # Skip header row and save in variable called headings
    headings = next(csvreader)
    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])
        # Add profit/loss to total_profit
        total_profit = total_profit + profit_loss
        
        # Count total months:
        total_months += 1

        # Compare Previous Profit/Loss to current Profit/Loss
        change = profit_loss - previous_profit_loss
        if total_months !=1:
        # Add change to changes [list], ignore the first line as there are no initial number to compare to for the first line of data
            changes.append(change)

        if change > greatest_inc:
            greatest_inc = change
            greatest_inc_month = date

        if change < greatest_dec:
            greatest_dec = change
            greatest_dec_month = date

        previous_profit_loss = profit_loss
        first_loop = False

avg_change = round((sum(changes)/len(changes)),0)

analysis = f"""

Total Profit: ${total_profit}
Total Months: {total_months}
Average Monthly Change: ${avg_change}
Greatest Increase: {greatest_inc_month}, ${greatest_inc}
Greatest Decrease: {greatest_dec_month}, ${greatest_dec}
"""
print(analysis)

 # Create a text file output of the final analysis
output_file = "output.txt"
with open(output_file, "w") as doc:
    doc.write(analysis)