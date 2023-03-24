# python-challenge
Module 3 - Python Challenge

This repository includes both the PyBank and PyPoll assignments in the Module 3 - Python Challenge.

    PyBank
    This challenge looks at the financial records of a company to learn information about its profit and loss activity. The python script reads the csv file provided, calculates various financial metrics, and exports the findings to a text file.

    This python script calculates the total number of months covered in the dataset, the total profit/loss, the average change in profit/loss, and the months with the greatest increase/decrease over the given period.

        Process
        First, the python script imports the relevant modules, opens the CSV file, and adds the relevant columns into lists. Then, for each row in the CSV, the script adds the P&L amounts to get to a total for the period.
        We then calculate the monthly change in P&L by taking the difference between the current month's P&L and the prior month's, using a loop to calculate for each row. No change is calculated for the first row because there was no prior month amount. These monthly changes are stored in another list so that we may calculate the average change and the max/min.
        Once all of the formulas are completed, we print the results to the terminal and to a text file.

        Conclusion
        86 months are covered in this analysis.
        The average monthly change in P&L over this time was a loss of $8,311.11. 
        The greatest increase in profits was in July 2016 at $1,862,002, and the greatest decrease was in January 2014 at (-$1,825,558).

    PyPoll
    This challenge analyzes the voting results of a local election to determine which candidate won. The python script creates a list of all candidates receiving votes, tallies how many votes each candidate received, and declares a winner.

        Process
        The python script opens the CSV file and defines the necessary variables.
        It counts the number of rows in the CSV to determine the number of votes cast.
        We then create a list of candidates receiving votes by looking at the unique entries in the voting list.
        We count the number of votes a candidate received by counting the number of times their name appears in the "vote" list.
        To calculate the percentage of votes received, we take the calculated votes received by each candidate and divide by the total number of votes.
        We then create a dictionary to store the candidate information, with a key for name, number of votes, and percent of votes. Each key connects to a list of the calculated data. 
        Finally we calculate the winner of the election by determining who received the highest number of votes and returning the candidate associated with that number.


        Conclusion
        With 369,711 total votes cast, the winner of this election is Diana DeGette with 272,892 votes or 73.812% of the vote.
