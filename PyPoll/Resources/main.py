
import os
import csv
csvpath = os.path.join("..", "Resources", "election_data.csv")
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # delete header
    header = next(csvreader)
    
    totalvotes = 0
    candidates =[]
    percentages = []
    cantotal = []
    khantotal = 0
    correytotal = 0
    litotal = 0
    tooleytotal = 0
    
    #calculate each candidates total vote
    for row in csvreader:
        totalvotes = totalvotes + 1
        candidates.append(row[2])
        if row[2] == "Khan":
            khantotal = khantotal + 1
        elif row[2] == "Correy":
            correytotal = correytotal + 1
        elif row[2] == "Li":
            litotal = litotal + 1
        else:
            tooleytotal = tooleytotal + 1
   
    #calculate candidate's percentage of votes
    khanpercen = khantotal/totalvotes
    correpercen = correytotal/totalvotes
    lipercen = litotal/totalvotes
    toolpercen = tooleytotal/totalvotes

    #add each candidate percentage votes to list
    percentages.append(khanpercen)
    percentages.append(correpercen)
    percentages.append(lipercen)
    percentages.append(toolpercen)

    #add each candidate's total votes to list
    cantotal.append(khantotal)
    cantotal.append(correytotal)
    cantotal.append(litotal)
    cantotal.append(tooleytotal)

    #delete duplicate names from list
    candidates = list(dict.fromkeys(candidates))
    print("Total Votes ", totalvotes)

    print(candidates)
    summary = zip(candidates, percentages, cantotal)
    for i in summary:
        print(i)

    #find the winner
    if khantotal > correytotal and khantotal > litotal and khantotal > tooleytotal:
        winner = "Khan"
        print("Khan is the winner")
    elif correytotal > khantotal and correytotal > litotal and correytotal > tooleytotal:
        winner = "Correy"
        print("Correy is the winner")
    elif litotal > khantotal and litotal > correytotal and litotal > tooleytotal:
        winner = "Li"
        print("Li is the winner")
    else:
        winner = "Tooley"
        print("Tooley is the winner")

with open("summary.txt", "a") as f:
    print(f"Election Results", file = f)
    print(f"---------------------------------------------------------------", file = f)
    print(f"Total number of votes casted in the election: {totalvotes}", file = f)
    print(f"---------------------------------------------------------------", file = f)
    for i in summary:
        print(i, file = f)
    print(f"---------------------------------------------------------------", file = f)
    print(f"The winner of the election is: {winner}", file = f)
f.close() 