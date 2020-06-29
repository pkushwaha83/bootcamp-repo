# Modules
import os
import csv



# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

Candidate = []
TotalCandidate = []
CVoteCount = []
CVotePercent = []
count = 0

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip headers
    next(csvreader, None)
    for row in csvreader:
        count = count + 1
        Candidate.append(row[2])
    for x in set(Candidate):
        TotalCandidate.append(x)
        CCount = Candidate.count(x)
        CVoteCount.append(CCount)
        CVotePercent.append(Candidate.count(x)/count)

    Winner = TotalCandidate[CVoteCount.index(max(CVoteCount))]
    #print(Winner)

with open('Election_Results.txt', 'w') as text:
        text.write("Election Results for file 'election_data.csv'"+"\n")
        text.write("----------------------------------------------------------\n")
        text.write("Total Vote: " + str(count) + "\n")
        text.write("----------------------------------------------------------\n")
        for i in range(len(set(Candidate))):
            text.write(TotalCandidate[i] + ": " + str(round(CVotePercent[i]*100,1)) +"% (" + str(CVoteCount[i]) + ")\n")
        text.write("----------------------------------------------------------\n")
        text.write("Winner: " + Winner +"\n")
        text.write("----------------------------------------------------------\n")




