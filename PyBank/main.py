import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")

total_month = 0
net_total = 0
changes = []
count = []
increase = 0
decrease = 0
increasemonth = 0
decreasemonth = 0
totalchanges = 0


#read file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    row = next(csvreader)

# total months and profit
    initialprofit = int(row[1])
    total_month = total_month +1
    net_total = net_total + int(row[1])



#make loop to read through all data
    for row in csvreader:

        total_month = total_month +1
        net_total = net_total + int(row[1])

#average of changes: total change between months/ months
        
        finalprofit = int(row[1])
        profitchanges = finalprofit - initialprofit
        changes.append(profitchanges)
        initialprofit = finalprofit
        count.append(row[0])
        
        
#greatest increase/ decrease

        if int(row[1])> increase:
            increase = int(row[1])
            increasemonth = row[0]

        elif int(row[1]) < decrease:
            decrease = int(row[1])
            decreasemonth = row[0]

    avgchanges = sum(changes)/len(changes)
    
    high = max(changes)
    low = min(changes)

print ("Financial Analysis")
print ("-------------------------")
print ("Total Months: " + str(total_month))
print ("Total: $" + str(net_total))
print ("Average Change: $" + str(avgchanges))
print ("Greatest Increase in Profits: " + str(increasemonth) + "(" + str(high) + ")")
print ("Greatest Decrease in Profits: " + str(decreasemonth) + "(" + str(low) + ")")

f = open("PyBank.txt", "w")
f.write("Financial Analysis\n")
f.write("-------------------------\n")
f.write("Total Months: " + str(total_month)+ "\n")
f.write("Total: $" + str(net_total)+ "\n")
f.write("Average Change: $" + str(avgchanges)+ "\n")
f.write("Greatest Increase in Profits: " + str(increasemonth) + "(" + str(high) + ")\n")
f.write("Greatest Decrease in Profits: " + str(decreasemonth) + "(" + str(low) + ")\n")
f.close()
