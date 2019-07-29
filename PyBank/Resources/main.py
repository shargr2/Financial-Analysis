import os
import csv
csvpath = os.path.join("..", "Resources", "budget_data.csv")
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # delete header
    header = next(csvreader)
   
    totalmonths = 0
    nettotal = 0
    totals = []
    monthlychange =[]

    for row in csvreader:
        #calculate total months
        totalmonths = totalmonths + 1
        #calculate net total
        nettotal = nettotal + int(row[1])
        #calculate monthly changes by making new lists of monthly totals
        totals.append(int(row[1]))
    print("Total months = ", totalmonths)
    print("Net total = $", nettotal)

    #created list of monthly changes
    for i in range(0,len(totals)-1):
        change = int(totals[i+1]) - int(totals[i])
        monthlychange.append(change)
   
    #calculate average monthly changes
    monthlychangetotal = 0
    for i in range(0,len(monthlychange)):
        monthlychangetotal = monthlychangetotal + monthlychange[i]
    average = monthlychangetotal/len(monthlychange)
    print("The average of the changes in Profit/Losses over the entire period $", average)

    #Calculate greatest increase in profits
    for i in range(0,len(monthlychange)-1):
        if monthlychange[i+1] > monthlychange[i]:
            greatest = monthlychange[i + 1]
        else:
            greatest = monthlychange[i]
    print("The greatest increase in profits was $", greatest)

    #Calculate the greatest lost
    for i in range(0,len(monthlychange)-1):
        if monthlychange[i+1] < monthlychange[i]:
            least = monthlychange[i+1]
        else:
            least = monthlychange[i]
    print("The greatest decrease in profit was $", least)

with open("summary.txt", "a") as f:
    print(f"Budget Data Summary", file = f)
    print(f"---------------------------------------------------------------", file = f)
    print(f"Total months ={totalmonths}", file = f)
    print(f"Net total = ${nettotal}", file = f)
    print(f"The average of the changes in Profit/Losses over the entire period ${average}", file = f)
    print(f"The greatest increase in profits was ${greatest}", file = f)
    print(f"The greatest decrease in profit was $ {least}", file = f)
f.close() 
