import os
import csv

pollCSV = os.path.join('poll_data.csv')
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.



with open(pollCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    
    
   # print("Total Months", (row_count - 1), file=open("pybank.txt", "a"))
    print("Election Results ", file=open("pybank.txt", "a"))
    print("------------------------------------- ", file=open("pybank.txt", "a"))
    
    print("Total Votes: ", file=open("pybank.txt", "a"))

    print("------------------------------------- ", file=open("pybank.txt", "a"))
    print("Khan: ", file=open("pybank.txt", "a"))
    print("Correy ", file=open("pybank.txt", "a"))
    print("Li:  ", file=open("pybank.txt", "a"))
    print("O'Tooley:  ", file=open("pybank.txt", "a"))
    print("------------------------------------- ", file=open("pybank.txt", "a"))
    print("Winner: ", file=open("pybank.txt", "a"))
    print("------------------------------------- ", file=open("pybank.txt", "a"))
    
    
   



    




   

