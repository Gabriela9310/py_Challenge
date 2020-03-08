import os
import csv
ele_info=os.path.join("election_data.csv")

with open(ele_info)as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    

    
    print("Election Results")
    print("................................................................................")

    row_count = sum(1 for row in csvreader)
    print(f'Total months: {row_count}')
