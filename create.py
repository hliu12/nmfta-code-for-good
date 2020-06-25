# Andrew Crofts and Ann Marie Burke
# Code for Good - NMFTA
# June 2020
# creates new entry for blacklist


import requests
import datetime
import random

# define constants as min and max time in hours
MIN = 8
MAX = 24 

"""
# Name: current_time
# Purpose: return current UTC time
# Input: none
# Returns: string of current UTC time in ISO 8601 format as specified in
# https://nmftabouncer.docs.apiary.io/#introduction/working-with-date-and-time
# Effects: calls utcnow function through datetime module
"""
def current_time():
    return datetime.datetime.utcnow().isoformat()

"""
# Name: random_time
# Purpose: calculates random time duration to pass from start time
# Input: none
# Returns: string of random UTC time between 8 and 24 hours
#          later than current_time (end time)
# Effects: prints start time, duration, and end time
"""
def random_time(curr):
    current_time = datetime.datetime.utcnow().isoformat() # set variable type
    current_time = curr

    # get datetime format from ISO format to be compatible with duration
    current_time = datetime.datetime.fromisoformat(str(curr))
    print("Start time " + str(curr))

    # get random number between MIN and MAX
    random_num = (random.random() * (MAX - MIN)) + MIN

    # set duration to be random_num hours
    duration = datetime.timedelta(hours=random_num)
    print("Duration of block: " + str(duration))
    
    # random end time is current time + duration
    random_end = current_time + duration
    end_time = random_end.isoformat() # ISO format
    print("End time: " + str(end_time))

    return end_time

"""
# Name: create
# Purpose: accesses the create function of the API to create an entry
# Input: none
# Returns: none
# Effects: calls current_time and random_time to get start and end times for entry
"""
def create():
    start_time = current_time()
    end_time = random_time(start_time)
    headers = {
        'Authorization': 'Bearer {access token from /login}',
        'IP': '35.4.6.4.33/24',
        "Start_Date": start_time,
        "End_Date" : end_time,
    }

    request = requests.get('https://private-anon-31136030c9-nmftabouncer.apiary-mock.com/v1.1/blacklists/ipaddresses/create', params = headers)
    print('Status code: ' + str(request.status_code))
    print('Text: ' + str(request.text))
    #TODO: Print list to ensure IP is added

"""
# Name: main
# Purpose: main function
# Input: none
# Returns: none
# Effects: calls create() function
"""
def main():
    create()

#call main
main()


