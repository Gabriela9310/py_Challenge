import os
import csv
bank_info=os.path.join("budget_data.csv")
data_1=[]
with open(bank_info)as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    def print_amount(bank_data):
        csvfile.seek(0)
        next(csvreader)
        total_pyl=0
        for row in bank_data:
            total_am=int(row[1])
            total_pyl=total_pyl + total_am
        return total_pyl
    
    print("Financial analysis")
    print("................................................................................")

    row_count = sum(1 for row in csvreader)
    print(f'Total months: {row_count}')
    print('Total amount: '+ str(print_amount(csvreader)))