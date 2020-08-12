"""
# Code for Good - NMFTA
#
# timezone_geoblock.py
# Validates times of various time zones and 
# blocklists geolocations at improper times
#
# Written by Henry Liu
#       on July 2020
"""

import requests
import datetime
from dateutil.relativedelta import relativedelta
import random
import sys

import list_helpers

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
        ip = args[1]
        time_at_loc = get_time(ip)
        if (not validate_time(time_at_loc)) :
            to_blocklist = get_geo(ip)
            create(to_blocklist, time_at_loc)
        else:
            print("Time at timezone is valid")
    else:
        print("Please input a valid IP address")

"""
# Name: validate_time
# Purpose: Checks to see the time given is between 7AM - 10PM
# Input: The time to validates
# Returns: A boolean indicating if the time is valid
"""
def validate_time(time):
    if (time.hour >= 22 or time.hour  < 7):
        return False
    else: 
        return True

"""
# Name: get_time
# Purpose: gets the current time at the given IP address
# Input: IP address
# Returns: current datetime of IP address
"""
def get_time(ip):
    url = 'https://api.ipgeolocation.io/ipgeo?apiKey=1ae3774e2eb14f34a869994f603dbd05&ip=' + str(ip)
    # print(url) # debugging
    response = requests.get(url)
    # print(response.text) # debugging - print response text
    jsonResponse = response.json()
    time = str(jsonResponse["time_zone"]["current_time"])
    country = str(jsonResponse["country_name"])
    # Converts the json response time into a dateTime object
    print("Time at " + country + ": " + time) #prints time and country for debugging
    dateTime = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S.%f%z')
    #print(dateTime) #ensures string converesion success for debugging
    return dateTime

"""
# Name: create
# Purpose: create an entry in API blocklist
# Input: none
# Returns: none
# Effects: calls current_time and random_time to get start and end times for entry
"""
def create(to_blocklist, start_time):
    print("Adding " + str(to_blocklist) + " to blocklist...\n")
    # Calculates the next 7am to be the end time
    relative_days = (start_time.hour >= 7)
    absolute_kwargs = dict(hour=7, minute=0, second=0, microsecond=0)
    next7am = start_time + relativedelta(days=relative_days, **absolute_kwargs)
    end_time = next7am

    list_helpers.create_geo_entry("blocklist", to_blocklist, start_time, end_time)

"""
# Name: get_geo
# Purpose: get geo location country code of given IP address
# Input: IP address
# Returns: geo location country code of IP address
"""
def get_geo(ip):
    url = 'https://ipinfo.io/' + str(ip) + '/json'
    # print(url) # debugging
    response = requests.get(url)
    # print(response.text) # debugging - print response text
    jsonResponse = response.json()
    if "country" in jsonResponse.keys():
        country_code = str(jsonResponse["country"])
    else:
        sys. exit("Invalid IP.\n")
    # print(country_code) # debugging - print country code
    return country_code

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
# Name: main
# Purpose: main function
# Input: none
# Returns: none
# Effects: calls validate_time and create accordingly
#          to respond to login attempts at unusual times
"""
def main():
    process_args()

# call main
main()

