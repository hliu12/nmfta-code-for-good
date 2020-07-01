# Andrew Crofts
# Code for Good - NMFTA
# June 2020
# sends GET request to Bouncer API


import requests
import datetime

# Name: current_time
# Purpose: returns string of current UTC time
# Input: none
# Returns: string
# Effects: calls now function through datetime module
def current_time():
    #TODO: Implement
    parent = 14 #PLACEHOLDER
# STUB

# Name: random_time
# Purpose: returns string of random UTC time between 8 and 24 hours later than current_time
# Input: none
# Returns: string
# Effects:
def random_time(current_time):
    #TODO: Implement
    current_time = 23 #PLACEHOLDER
# STUB


# Name: try_create
# Purpose: accesses the create function of the API
# Input: none
# Returns: none
# Effects: calls requests get function
def try_create():
    current_time = current_time()
    random_time = random_time(current_time)
    headers = {
        'Authorization': 'Bearer {access token from /login}',
        'IP': '35.4.6.4.33/24',
        "Start_Date": current_time,
        "End_Date" : random_time
    }

    request = requests.get('https://private-anon-31136030c9-nmftabouncer.apiary-mock.com/v1.1/blacklists/ipaddresses/create', params = headers)
    print('Status code: ' + str(request.status_code))

    #TODO: Print list to ensure IP is added

# Name: main
# Purpose: main function
# Input: none
# Returns: none
# Effects: calls get_request_format function
def main():
    try_create()

#call main

main()


