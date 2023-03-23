# Import dependencies
import os
import csv

#Import csv file
csvpath = os.path.join("Resources", "budget_data.csv")

# Define variables
months = []
number_of_months = 0
profit_loss_total = 0
change = []
monthly_change = 0
total_change = 0

# Open CSV file and skip header
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Calculate total amount of profit/loss, monthly change, and total change
    prior_month_PL = 0       
    for row in csvreader:
        months.append((row[0]))
        profit_loss_total += int(row[1])
        if row[0] != "Jan-10":
            monthly_change = int(row[1]) - prior_month_PL
            change.append(monthly_change)
            prior_month_PL = int(row[1])
            total_change += int(monthly_change)
        else:
            prior_month_PL = int(row[1])          

    
    # Calculate number of months included in dataset
    number_of_months = len(months)
    
    # Calculate average of P&L change over entire period
    average_change = round(total_change / (len(change)),2)
    
    # Calculate greatest increase/decrease and determine which month this occurred
    greatest_increase = max(change)
    greatest_increase_row = change.index(max(change)) + 1
    greatest_decrease = min(change)
    greatest_decrease_row = change.index(min(change)) + 1
    
# Print results to terminal and to text file
line1 = "Financial Analysis"
line2 = "----------------------------"
line3 = "Total Months: " + str(number_of_months)
line4 = "Total: $" + str(profit_loss_total)
line5 = "Average Change: $" + str(average_change)
line6 = "Greatest Increase in Profits: " + str(months[greatest_increase_row]) + " ($" + str(greatest_increase) + ")"
line7 = "Greatest Decrease in Profits: " + str(months[greatest_decrease_row]) + " ($" + str(greatest_decrease) + ")"

output_info = [line1, line2, line3, line4, line5, line6, line7]

print("\n".join(output_info))

with open("analysis\output.txt", "w") as output:
    output.writelines("\n".join(output_info))