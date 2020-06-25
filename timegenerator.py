# Code for Good - NMFTA
#
# timegenerator.py
# Handles various time related operations
#
# Written by Henry Liu
#       on June 2020

from datetime import datetime, timedelta
from random import randint

# Name: main
# Purpose: main function
# Input: none
# Returns: none
# Effects: Prints current time, blacklist time and end times
def main(): 
    # Prints current time
    current_time = datetime.utcnow()
    print("The current time is: ")
    print(current_time)
    # Gets a random number of hours between 8-24
    blacklist_time = randint(8,24)
    # Calculates end time
    end_time = current_time + timedelta(hours=blacklist_time)
    print("After a blacklist time of " + str(blacklist_time) + " hours, the blacklist will expire at: " )
    print(end_time)

# Calls main
main()