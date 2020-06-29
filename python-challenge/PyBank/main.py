# Modules
import os
import csv



# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")
date = []
month = []
year = []
ProfitLoss = []
TotalPL = 0
Count = 0
PLBeg = 0
TotalPLChange = 0
PLChange = []


# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip headers
    next(csvreader, None)

    # Loop through looking for the video
    for row in csvreader:
        #splitdate = row[0].split('-')
        #print(row[0] + " is Date " + row[1] + " Profit / Loss ")
        #print(splitdate)
        #Append data from the row
        Count = Count + 1
        date.append(row[0])
        ProfitLoss.append(row[1])
        TotalPL = TotalPL + int(row[1])
        PLEnd = int(row[1])
        PLChg = PLEnd - PLBeg
        TotalPLChange = TotalPLChange + PLChg
        PLChange.append(PLChg)
        splitdate = row[0].split('-')
        month.append(str(splitdate[0]))
        year.append(splitdate[1][-2:])
        PLBeg = PLEnd
        #print(PLBeg)

AvePLChg = TotalPLChange / Count
#print(AvePLChg)
GIncrease = max(PLChange)
#print(GIncrease)
GDecrease = min(PLChange)
#print(GDecrease)
MaxDate = date[PLChange.index(GIncrease)]
#print(MaxDate)
MinDate = date[PLChange.index(GDecrease)]
#print(MinDate)
CountMonth = len(set(date))
#print(CountMonth)

with open('financial_analysis_report.txt', 'w') as text:
        text.write("Financial Analysis for file 'budget_data.csv"+"\n")
        text.write("----------------------------------------------------------\n")
        text.write("    Total Months: " + str(CountMonth) + "\n")
        text.write("    Total : " + "$" + str(TotalPL) +"\n")
        text.write("    Average Change: " + '$' + str(int(AvePLChg)) +'\n')
        text.write("    Greatest Increase in Profits: " + str(MaxDate) + " ($" + str(GIncrease) + ")\n")
        text.write("    Greatest Decrease in Profits: " + str(MinDate) + " ($" + str(GDecrease) + ")\n\n")