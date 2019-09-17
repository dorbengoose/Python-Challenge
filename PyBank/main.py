
# 1 .- Import Modules from Python Library (as in the Classroom)

# Allows to create the Open to Destination for the Bank.csv File to main.py
import os       # As in the Classroom

# Import Module to be able to read a CSV File in Python save as bank_statement
import csv      # As in the Classroom

# 2.-Variables and names Directory
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#   bank_statement:       The financial balance (month,amount)
#   bank_py:              The financial balance into Python
#   bank_list:            Getting into a list object
#   months:               Length of the list without bank_header
#   bank_numbers:         List of data in string, column 1
#   bank_integers:        List of Integers from bank_numbers
#   max_Profit:           Prints the Maximum Profit
#   min_Profit:           Prints the minimum Profit
#   Greatest_Increase     Gets the Greatest Average INCREASE
#   Greatest_Decrease     Gets the Greatest Average DECREASE
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Define the CSV Path, same directory as main.py (To Read it easier)
bank_statement = os.path.join("..", "Python-Challenge", "PyBank", "Bank.csv")

# 3 .- Develop the Executions

# Instruction to extract the data separated by comma('). Saving into .py extension
with open(bank_statement, newline='') as bank_statement:

    # CSV reader specifies delimiter and variable that holds contents
    # As in the Class
    bank_py = csv.reader(bank_statement, delimiter=',')
    print(bank_py)
    # Read the header row first (skip this step if there is now header)
    bank_header = next(bank_py)
    print(f"Bank Header: {bank_header}")
    bank_list = []
    # Assigning into a list
    bank_list = list((bank_py))
    # print(bank_list)
    # TOTAL MONTHS: Lenght of the List = 86
    months = len(bank_list)

    # Reads the data, colum 1 by row
    bank_numbers = [row[1] for row in bank_list]

    # converts to integer such list
    def convert(amount):
        return int(amount)
    bank_integers = list(map(convert, bank_numbers))

    # Getting the SUBSTRACCION from consecutive numbers, from PYTHON.ORG
    Changes_Amount = [t - s for s, t in zip(bank_integers, bank_integers[1:])]

    # Calculating the Average Change
    months = months-1
    Average_Change = float(sum(Changes_Amount)/months)

    # Calculating Greatest Increase
    # Calculating Greatest Decrease
    Greatest_Increase = max(Changes_Amount)
    Greatest_Decrease = min(Changes_Amount)

    print(f'The total Months are: {months}')
    # Prints the Total Profit:
    Total_Profit = sum(bank_integers)
    print(f'The Total Profit of the Balance is: {Total_Profit}')
    # Prints the Maximum Profit
    max_Profit = max(bank_integers)
    print(f'The Maximum Profit is: {max_Profit}')

    # Prints the Minimum Profit
    min_Profit = min(bank_integers)
    print(f'The Minimum Profit is: {min_Profit}')
    # Prints the Average Change
    print(f'The Average Change is: {Average_Change}')
    # Prints The Greatest INCREASE AND DECREASE
    print(f'The Greatest increase is: {Greatest_Increase}')
    print(f'The Greatest Decrease is: {Greatest_Decrease}')
    
    # EXPORTINT TO FILE TEXT NAMED Results_Bank
    # SYSTEM Module, from Python.org
    import sys

    sys.stdout = open('../Python-Challenge/PyBAnk/Results_Banks.txt', 'w')
    # Prints the Total Months
    print(f'The total Months are: {months}')
    # Prints the Total Profit:
    Total_Profit = sum(bank_integers)
    print(f'The Total Profit of the Balance is: {Total_Profit}')
    # Prints the Maximum Profit
    max_Profit = max(bank_integers)
    print(f'The Maximum Profit is: {max_Profit}')

    # Prints the Minimum Profit
    min_Profit = min(bank_integers)
    print(f'The Minimum Profit is: {min_Profit}')
    # Prints the Average Change
    print(f'The Average Change is: {Average_Change}')
    # Prints The Greatest INCREASE AND DECREASE
    print(f'The Greatest increase is: {Greatest_Increase}')
    print(f'The Greatest Decrease is: {Greatest_Decrease}')
    sys.stdout.close()