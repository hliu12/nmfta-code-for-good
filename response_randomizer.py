# Code for Good - NMFTA
#
# response_randomizer.py
# Template to randomize responses
#
# Written by Henry Liu
#       on June 2020

from random import randint

"""
# Name: main
# Purpose: main function
# Input: none
# Returns: none
# Effects: 
"""
def main(): 
    randResponse(3);


"""
# Name: randResponse
# Purpose: Template to call a random response out of many
# Input: Number of responses
# Returns: none
# Effects: Executes a random response
"""
def randResponse(numResponses):
    print("Calling response number: ", end = "")
    responseToCall = randint(1, numResponses)
    # Replace print statements with calls to response functions
    if (responseToCall == 1):
        print(responseToCall)
    elif (responseToCall == 2):
        print(responseToCall)
    else:
        print(responseToCall)



# Calls main
main()