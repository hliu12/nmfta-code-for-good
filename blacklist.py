# Andrew Crofts and Ann Marie Burke
# Code for Good - NMFTA
# June 2020
# creates new entry for blacklist with random time duration


import requests
import datetime
import random
import sys

# define constants as min and max time in hours
MIN = 8
MAX = 24 

"""
# Name: current_time
# Purpose: return current UTC time
# Input: none
# Returns: string of current UTC time in ISO format
# Effects: calls utcnow function through datetime module
"""
def current_time():
    return datetime.datetime.utcnow().isoformat()

"""
# Name: random_time
# Purpose: calculates random time duration
#          and calculates end time from given start time
# Input: none
# Returns: string of random UTC time in ISO format between 8 and 24 hours
#          later than current_time (end time)
# Effects: prints start time, duration, and end time
"""
def random_time(curr):
    # get datetime format from ISO format to be compatible with duration
    current_time = datetime.datetime.fromisoformat(str(curr))
    print("Start time " + str(curr))

    # get random number between MIN and MAX
    random_num = (random.random() * (MAX - MIN)) + MIN

    # set duration to be random_num hours
    # https://docs.python.org/3/library/datetime.html#datetime.timedelta
    duration = datetime.timedelta(hours=random_num)
    print("Duration of block: " + str(duration))
    
    # random end time is current time + duration
    random_end = current_time + duration
    end_time = random_end.isoformat() # convert to ISO format
    print("End time: " + str(end_time))

    return end_time

"""
# Name: ip_params
# Purpose: parameters to add ip address
# Input: ip address, start time, end time (all as string vars)
# Returns: params for request
"""
def ip_params(ip, start_time, end_time):
    params = {
        "IP": ip,
        "Start_Date": start_time,
        "End_Date" : end_time,
    }

    return params

"""
# Name: geo_params
# Purpose: parameters to add geo location
# Input: geo location, start time, end time (all as string vars)
# Returns: params for request
"""
def geo_params(geo, start_time, end_time):
    params = {
        "Country Code": geo,
        "Start_Date": start_time,
        "End_Date" : end_time,
    }

    return params

"""
# Name: create
# Purpose: create an entry in API blacklist
# Input: none
# Returns: none
# Effects: calls current_time and random_time to get start and end times for entry
"""
def create(type, to_blacklist):
    # TODO: add error handling when invalid IP or Geo Location
    print("Adding " + str(to_blacklist) + " to blacklist...\n")

    start_time = current_time()
    end_time = random_time(start_time)
    headers = {
        'Authorization': 'Bearer {access token from /login}',
    }

    if (type == 'ip'):
        params = ip_params(to_blacklist, start_time, end_time)
    elif (type == 'geo'):
        params = geo_params(to_blacklist, start_time, end_time)
    else:
        print("Error: Invalid entry")
        pass
    
    request = requests.post('https://private-anon-31136030c9-nmftabouncer.apiary-mock.com/v1.1/blacklists/ipaddresses/create', headers=headers, params=params)
    print('Status code: ' + str(request.status_code))
    print('Text: ' + str(request.text))
    print('\n')
    # TODO: Search list to ensure IP is added

"""
# Name: main
# Purpose: main function
# Input: none
# Returns: none
# Effects: calls create function on ip and geo location
"""
def main():
    args = sys.argv # get args
    argc = len(args) # get num of args

    if (argc == 2):
        flag = args[1]
        if (flag == "--help"):
            print("Usage: --help for help")
            print("       --ip [IP address]")
            print("       --geo [Geo Location]")
        else:
            print("Use --help to get started.")
    elif (argc != 3):
        print("Use --help to get started.")
    else:
        flag = args[1]
        to_blacklist = str(args[2])
        if (flag == "--ip"):
            create('ip', to_blacklist)
        elif (flag == "--geo"):
            create('geo', to_blacklist)
        else:
            print("Error: Invalid flag")

# call main
main()

# Resources:
#   https://docs.python.org/3/library/random.html
#   https://docs.python.org/3/library/datetime.html
#   https://stackoverflow.com/questions/2150739/iso-time-iso-8601-in-python
#   https://www.geeksforgeeks.org/get-current-date-and-time-using-python/#:~:text=To%20get%20both%20current%20date,current%20local%20date%20and%20time.

