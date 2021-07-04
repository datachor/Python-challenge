import os
import csv

path="budget_data.csv"

with open(csvpath) as csvfile:
    csvreader = csv.reader(file)
    data=[]
    for row in csvreader:
        data.append(row)

    print(data)

    











