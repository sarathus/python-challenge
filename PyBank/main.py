#PyBank
# Created By Sarath K - 2019.06.13

import os
import csv
minimum = 0
maximum = 0
months=0
PandL=0
past_month=0
monthly_change=0
tot_monthly_change=-0.0
# Read budget.csv file
budget_csv = 'budget_data.csv'

Total_PandL=0.0
with open(budget_csv, 'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    header=next(csvreader)

    for row in csvreader:
    # Sums total profit and loss
        Total_PandL = Total_PandL+int(row[1])
    # Counts total months to use on average revenue
        months += 1
        #for i in range(1,len(row)):
        monthly_change=int(row[1])-past_month
        tot_monthly_change = tot_monthly_change + monthly_change
        past_month=int(row[1])
        if minimum > monthly_change:
            minimum = monthly_change
            Date1=str(row[0])
        if maximum < monthly_change:
            maximum=monthly_change
            Date2=str(row[0])
           
    #Average=Total_PandL/months
    Average=tot_monthly_change / (months-1)
   

    print("\nFinancial Analysis")
    print("----------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${Total_PandL}")
    print(f"Average: ${Average}")
    print(f"Greatest increase in profit on {Date2} is ${maximum}")
    print(f"Greatest decrease in profit on {Date1} is ${minimum}\n")

text_file = open("pybankoutput.txt", "w")

text_file.write(f"\nFinancial Analysis\n----------------------\nTotal Months: {months}\nTotal: ${Total_PandL}\nAverage: ${Average}\nGreatest increase in profit on {Date2} is ${maximum}\nGreatest decrease in profit on {Date1} is ${minimum}\n")

text_file.close()
        
