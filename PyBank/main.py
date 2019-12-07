import os
import csv

# point to csv file
os.chdir(os.path.dirname(os.path.abspath(__file__))) 
budget_csv = os.path.join(".", "Resources", "budget_data.csv")

# initialize lists
month_list = []
monthly_pl = []

# add row index 0 to monthly_list, index 1 to monthly_pl
with open(budget_csv, "r", newline="") as csvfile:
    #separate data with comments
    csvreader = csv.reader(csvfile, delimiter=",")
    # skip header
    header = next(csvreader)
    for row in csvreader:
        month_list.append(row[0])
        monthly_pl.append(row[1])

# convert monthly_pl items to int using list comprehension
monthly_pl = [int(pl) for pl in monthly_pl]

# calculate total number of months
total_months = len(month_list)
# calculate net total amount of p&l over the entire period
net_pl = sum(monthly_pl)
# create new list of monthly p&l change 
pl_change_monthly = [monthly_pl[i + 1] - monthly_pl[i] for i in range(len(monthly_pl)-1)]
# calculate the average of the changes in p&l over the entire period, rounded to 2 decimals
avg_pl = round((sum(pl_change_monthly))/len(pl_change_monthly), 2)
# calculate the greatest increase in profits & greatest decrease in losses
greatest_profit = max(pl_change_monthly)
greatest_loss = min(pl_change_monthly)
# retrieve index number for greatest changes in both directions
p = pl_change_monthly.index(greatest_profit)
l = pl_change_monthly.index(greatest_loss)
# match index number to month
best_month = month_list[p+1]
worst_month = month_list[l+1]

results = (
    "Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {str(total_months)}\n"
    f"Total: ${str(net_pl)}\n"
    f"Average Change: ${str(avg_pl)}\n"
    f"Greatest Increase in Profits: {best_month} (${str(greatest_profit)})\n"
    f"Greatest Decrease in Profits: {worst_month} (${str(greatest_loss)})\n"
)

print(results)

# specify output text file
budget_txt = os.path.join(".", "budget_data.txt")

# create .txt file
with open(budget_txt, "w") as txt:
    txt.write(results)