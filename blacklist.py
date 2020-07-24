"""
# Andrew Crofts, Ann Marie Burke, and Henry Liu
# Code for Good - NMFTA
# June - July 2020
# randomly creates new entry for blacklist with randomized time
#     and randomized response (either blocks IP or blocks all IPs from location)
"""

import requests
import datetime
import random
import sys
from random import randint

# define constants as min and max time in hours
MIN = 8
MAX = 24 
BLACKLIST_URL = "https://private-anon-31136030c9-nmftabouncer.apiary-mock.com/v1.1/blacklists/"
IP_INFO = "https://ipinfo.io/"

"""
# Name: print_usage
# Purpose: print usage for script
# Input: none
# Returns: none
"""
def print_usage():
    print("Usage: --help for help")
    print("       --ip [IP Address]")
    print("       --geo [IP Address of location to block]")
    print("       --random [IP Address] for random response")

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

    if (type == 'ip' or type == 'geo'):
        create_url = ""
        if (type == 'ip'):
            params = ip_params(to_blacklist, start_time, end_time)
            create_url = BLACKLIST_URL + "ipaddresses/create"
        elif (type == 'geo'):
            params = geo_params(to_blacklist, start_time, end_time)
            create_url = BLACKLIST_URL + "geolocations/create"
        request = requests.post(create_url, headers=headers, params=params)
        print('Status code: ' + str(request.status_code))
        print('Text: ' + str(request.text))
        print('\n')
        # TODO: Search list to ensure IP is added
    else:
        print("Error: Invalid entry")
        pass


"""
# Name: get_geo
# Purpose: get geo location country code of given IP address
# Input: IP address
# Returns: geo location country code of IP address
"""
def get_geo(ip):
    url = IP_INFO + str(ip) + '/json'
    # print(url) # debugging
    response = requests.get(url)
    # print(response.text) # debugging - print response text
    jsonResponse = response.json()
    # TODO: Account for invalid IP addresses, they currently crash the code due to 
    # line 130 not finding a "country" parameter
    if "country" in jsonResponse.keys():
        country_code = str(jsonResponse["country"])
    else:
        sys.exit("Invalid IP.\n")
    # print(country_code) # debugging - print country code
    return country_code

"""
# Name: randResponse
# Purpose: call a random response (either geo or ip)
# Input: A string IP address
# Returns: none
# Effects: calls create function to execute response
"""
def randResponse(ip):
    print("Executing random response: ", end = "")
    responseToCall = randint(1, 2)
    if (responseToCall == 1):
        print("ip blacklist")
        create('ip', ip)
    else:
        print("geolocation block")
        geo = get_geo(ip)
        create('geo', geo)

"""
# Name: validIP
# Purpose: check if an IP Address is valid IPv4
# Input: IP to check
# Returns: True if valid, False if not
"""
# TODO: fix some edge cases --> special IPs that can't be used
def validIP(ip):
    if ip.count('.') == 3:
        if (ip == '0.0.0.0' or ip == '255.255.255.255'):
            return False
        else:
            ipSplit = ip.split('.')
            return (len(ipSplit) == 4 and all(0 <= int(i) <= 255 for i in ipSplit))
    # elif ip.count(':') == 7:
    #     ipSplit = ip.split(':')
    #     for i in ipSplit:
    #         if len(i) > 4:
    #             return False
    #         return int(i, 16) >= 0 and i[0] != '-'
    else:
        return False

"""
# Name: process_args
# Purpose: process command line arguments
# Input: none
# Returns: none
"""
def process_args():
    args = sys.argv # get args
    argc = len(args) # get num of args

    if (argc == 2):
        flag = args[1]
        if (flag == "--help"):
            print_usage()
        else:
            print("Use --help to get started.")
    elif (argc != 3):
        print("Use --help to get started.")
    else:
        flag = args[1]
        
        ip = str(args[2])

        # if (validIP(ip)):
        if (flag == "--ip"):
            create('ip', ip)
        elif (flag == "--geo"):
            to_blacklist = get_geo(ip)
            create('geo', to_blacklist)
        elif (flag == "--random"):
            randResponse(ip)
        else:
            print_usage()
        # else:
        #     print("Not a valid IP address.")

"""
# Name: main
# Purpose: main function
# Input: none
# Returns: none
# Effects: calls process_args function to process command line arguments
"""
def main():
    process_args()

# call main
main()

"""
# Resources:
#   https://docs.python.org/3/library/random.html
#   https://docs.python.org/3/library/datetime.html
#   https://stackoverflow.com/questions/2150739/iso-time-iso-8601-in-python
#   https://www.geeksforgeeks.org/get-current-date-and-time-using-python/#:~:text=To%20get%20both%20current%20date,current%20local%20date%20and%20time.
#   https://www.tutorialspoint.com/validate-ip-address-in-python
"""

