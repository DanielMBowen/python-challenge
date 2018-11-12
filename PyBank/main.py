import os
import csv

budgetCSV = os.path.join('budget_data.csv')

#def getNumbers(budgetdata):
   
    #The total net amount of "Profit/Losses" over the entire period
    #The average change in "Profit/Losses" between months over the entire period
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in losses (date and amount) over the entire period


with open(budgetCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
     #The total number of months included in the dataset
    row_count = sum(1 for line in open(budgetCSV))
    print(row_count - 1)
   # print("Total Months", (row_count - 1), file=open("pybank.txt", "a"))
    print("Financial Analysis ", file=open("pybank.txt", "a"))
    print("------------------------------------- ", file=open("pybank.txt", "a"))
    
    print("Total Months: ", (row_count - 1), file=open("pybank.txt", "a"))
    print("Total: ", file=open("pybank.txt", "a"))
    print("Average Change ", file=open("pybank.txt", "a"))
    print("Greatest Increase in Profits:  ", file=open("pybank.txt", "a"))
    print("Greatest Decrease in Profits:  ", file=open("pybank.txt", "a"))
    
    
    #net_pos = sum(i for i in (int(budgetCSV[2])) if i > 0)



    




   

