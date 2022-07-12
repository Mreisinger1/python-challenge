#import os module
import os
#module for reading csv files
import csv

#file path
csvpath = os.path.join("Resources","budget_data.csv")

#define variables
profit = []
monthly_changes = []
date = []
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0
final_profit = 0
average_change_profits = 0
greatest_increase_profits = 0
greatest_decrease_profits = 0


#open csv path 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #for loop to find all data
    for row in csvreader:    

      count = count + 1 

      date.append(row[0])

      profit.append(row[1])

      total_profit = total_profit + int(row[1])

      final_profit = int(row[1])

      monthly_change_profits = final_profit - initial_profit

      monthly_changes.append(monthly_change_profits)

      total_change_profits = total_change_profits + monthly_change_profits

      initial_profit = final_profit

      average_change_profits = (total_change_profits/count)
      
      greatest_increase_profits = max(monthly_changes)

      greatest_decrease_profits = min(monthly_changes)

      increase_date = date[monthly_changes.index(greatest_increase_profits)]

      decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
    
    #print results to terminal 
    print("Financial Analysis")
    print("Total Months: " + str(count))
    print("Total: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
#print results to a text file 
with open ('budget_data.txt', 'w') as text:
    text.write("Financial Analysis"+ "\n")
    text.write("Total Months: " + str(count) +"\n")
    text.write("Total: " + "$" + str(total_profit) +"\n")
    text.write("Average Change: " + "$" + str(int(average_change_profits)) +"\n")
    text.write("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")" +"\n")
    text.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")

    

