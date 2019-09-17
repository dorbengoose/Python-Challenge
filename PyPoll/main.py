# # 1 .- Import Modules from Python Library (as in the Classroom)

#     #Allows to create the Open to Destination for the Bank.csv File to main.py
import os       # As in the Classroom

#     # Import Module to be able to read a CSV File in Python save as bank_statement
import csv      # As in the Classroom
import collections  # Imports the counter method for selecting data
#     # Define the CSV Path, same directory as main.py (To Read it easier)
poll = os.path.join("..", "Python-Challenge", "PyPoll", "Poll.csv")

#      #  2.-Variables and names Directory
# #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#     #   total_votes:          List, includes Calculates the Total Votes
#     #   poll_py:              The poll list into Python
#     #   tvi:                  Total Votes as Integer
# #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# #
# # 3 .- Develop the Executions

#     # Instruction to extract the data separated by comma('). Saving into .py extension
with open(poll, newline='') as poll:

    #     # CSV reader specifies delimiter and variable that holds contents
    #     # As in the Class
    poll_py = csv.reader(poll, delimiter=',')
    print(poll_py)
#         # Read the header row first (skip this step if there is now header)
    poll_header = next(poll_py)
    print(f"Poll Header: {poll_header}")

    # Defining Column 2 for Candidates Column

    total_votes = [row[2] for row in poll_py]

    # ******************************************************
    # From Collections module as extracted from Python.org
    # ******************************************************
    # Arrange the values in order according to ocurrence
    total_votes.sort()
    # Get the len from the list for getting total votes
    y = len(total_votes)
    print(f'The total Votes are: {y}')
    # Gets the whole ranking in to candidates_ranking list
    candidates_ranking = collections.Counter(total_votes)
    # Prints the whole candidate ranking
    print(f'The WHOLE ELECTION RESULTS are as follows:\n {candidates_ranking}')
    # Separate each Candidate values
    khan = int(candidates_ranking['Khan'])
    correy = int(candidates_ranking['Correy'])
    li = int(candidates_ranking['Li'])
    # Double quotes for O'Tooley
    otooley = int((candidates_ranking["O'Tooley"]))
    # Assigning an integer to tvi, Total Voters Integer
    tvi = int(y)
    # Calculating Percentages for each Candidate against total_votes, printing

    print('The winner is Khan with: {:.0%}'.format(
        khan/tvi) + ','+f' {khan} votes')
    print('The second place is for Correy with: {:.0%}'.format(
        correy/tvi) + ','+f' {correy} votes')
    print('The third place is for Li with: {:.0%}'.format(
        li/tvi) + ','+f' {li} votes')
    print("The fouth place is for O'Tooley with: {:.0%}".format(
        otooley/tvi) + ','+f' {otooley} votes')

    print(f'The absolute winner is Khan : {khan}')
    
    
    # EXPORTINT TO FILE TEXT NAMED RESULTS ELECTIONS
    # SYSTEM Module, from Python.org
    import sys

    sys.stdout = open('../Python-Challenge/PyPoll/Results_Elections.txt', 'w')

    print(f'The total Votes are: {y}')
    print(f'The WHOLE ELECTION RESULTS are as follows:\n {candidates_ranking}')
    print('The winner is Khan with: {:.0%}'.format(
        khan/tvi) + ','+f' {khan} votes')
    print('The second place is for Correy with: {:.0%}'.format(
        correy/tvi) + ','+f' {correy} votes')
    print('The third place is for Li with: {:.0%}'.format(
        li/tvi) + ','+f' {li} votes')
    print("The fouth place is for O'Tooley with: {:.0%}".format(
        otooley/tvi) + ','+f' {otooley} votes')
    print(f'The absolute winner is Khan: {khan}')
    sys.stdout.close()
