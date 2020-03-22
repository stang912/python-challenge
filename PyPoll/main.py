import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

totalvotes = 0
candidates = []
namesvotes = []
percent = []

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        totalvotes = totalvotes +1

        candidate = row[2]

        if candidate in candidates:
            names = candidates.index(candidate)
            namesvotes[names] = namesvotes[names] + 1

        else:
            candidates.append(candidate)
            namesvotes.append(1)

for n in namesvotes:
    percent.append(round(n/totalvotes *100, 1))

winner = candidates[namesvotes.index(max(namesvotes))]


print("Election Results")   
print("-------------------------")
print("Total Votes: " + str(totalvotes))    
print("-------------------------")

for x in candidates:
    print(x + ": " + str((percent[candidates.index(x)])) + "% (" + str(namesvotes[candidates.index(x)]) + ")")

print("-------------------------")
print("Winner: " + str(winner))
print("-------------------------")
    

f = open("PyPoll.txt", "w")
f.write("Election Results\n")   
f.write("-------------------------\n")
f.write("Total Votes: " + str(totalvotes) + "\n")    
f.write("-------------------------\n")

for x in candidates:
    f.write(x + ": " + str((percent[candidates.index(x)])) + "% (" + str(namesvotes[candidates.index(x)]) + ")\n")

f.write("-------------------------\n")
f.write("Winner: " + str(winner) +"\n")
f.write("-------------------------\n")

