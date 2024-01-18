#Import 
import csv

#Read csv file
with open('budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

    #variables
    months = []
    profits_losses = []
    changes = []

    #find total months and total profits/losses
    for row in csvreader:
        months.append(row[0])
        profits_losses.append(int(row[1]))

#calculate total months
total_months = len(months)

#total profits and losses
total_profits_losses = sum(profits_losses)
    
#Calculate changes in profits and losses and put it into a list
for i in range(1, total_months):
    change = profits_losses[i] - profits_losses[i-1]
    changes.append(change)

#Average change
average_change = sum(changes) / len(changes)

#Greatest increase and decrease
greatest_increase = max(changes)
greatest_increase_date = months[changes.index(greatest_increase) + 1]
greatest_decrease = min(changes)
greatest_decrease_date = months[changes.index(greatest_decrease) + 1]

#Print analysis results
print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profits_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Profit Increase: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Profit Decrease: {greatest_decrease_date} (${greatest_decrease})") 

#Create text file
output_file = "budget_results.txt"
#Write results into file
with open(output_file, "w") as file:
    file.write("Financial Analysis\n")
    file.write("-" * 40 + "\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profits_losses}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Profit Increase: {greatest_increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Profit Decrease: {greatest_decrease_date} (${greatest_decrease})\n") 


