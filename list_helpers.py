"""
# Ann Marie Burke
# Code for Good - NMFTA
# June - August 2020
# list_helpers.py -- helper functions for blocklisting/passlisting
#                    for NMFTA Bouncer
"""

import sys
import requests

# define constants
IP = "ip"
GEO = "geo"
URL = "https://private-anon-b3f9d4c760-nmftabouncer.apiary-mock.com/v1.1/"
BLOCK = "blocklist"
PASS = "passlist"


"""
# Name: create_ip_entry
# Purpose: create IP entry on blocklist or passlist (blacklist or whitelist)
# Input: rule - blocklist or passlist?
#        ip_version - IPv4 or IPv6
#        ip - IP address to block/pass
#        start_time - start time in UTC, formatted using ISO 8601 string format
#        end_time - end time in UTC, formatted using ISO 8601 string format
# Returns: none
# Effects: calls current_time and random_time to get start and end times for entry
"""
def create_ip_entry(rule, ip_version, ip, start_time, end_time):
    # TODO: error handling if start time is after end time
    headers = {
        'Authorization': 'Bearer {access token from /login}',
    }

    create_url = ""

    # TODO: add error handling for invalid IPs
    if (ip_version == 4):
        params = {
            "IPv4": ip,
            "Start_Date": start_time,
            "End_Date" : end_time,
        }
    elif (ip_version == 6):
        params = {
            "IPv6": ip,
            "Start_Date": start_time,
            "End_Date" : end_time,
        }
    else:
        print("ERROR: Unknown IP version", file=sys.stderr)

    if (rule == BLOCK):
        create_url = URL + "/blacklists/ipaddresses/create"
    elif (rule == PASS):
        create_url = URL + "/whitelists/ipaddresses/create"
    else:
        print("ERROR: Unknown rule", file=sys.stderr)
        pass

    if (create_url != ""):
        request = requests.post(create_url, headers=headers, params=params)
        if (request.status_code == 200):
            print('Success.\n')
        else:
            print('Error.\n')
    # TODO: Search list to ensure IP is added
    else:
        pass

"""
# Name: create_geo_entry
# Purpose: create geolocation entry on blocklist or passlist (blacklist or whitelist)
# Input: rule - blocklist or passlist?
#        geolocation - country code to block/pass
#        start_time - start time in UTC, formatted using ISO 8601 string format
#        end_time - end time in UTC, formatted using ISO 8601 string format
# Returns: none
# Effects: calls current_time and random_time to get start and end times for entry
"""
def create_geo_entry(rule, geolocation, start_time, end_time):
    # TODO: error handling if start time is after end time
    headers = {
        'Authorization': 'Bearer {access token from /login}',
    }

    # TODO: add error handling for invalid geolocations
    params = {
        "Country Code": geolocation,
        "Start_Date": start_time,
        "End_Date" : end_time,
    }

    create_url = ""

    if (rule == BLOCK):
        create_url = URL + "/blacklists/ipaddresses/create"
    elif (rule == PASS):
        create_url = URL + "/whitelists/ipaddresses/create"
    else:
        print("ERROR: Unknown rule", file=sys.stderr)
        pass

    if (create_url != ""):
        request = requests.post(create_url, headers=headers, params=params)
        if (request.status_code == 200):
            print('Success.\n')
        else:
            print('Error.\n')
    # TODO: Search list to ensure IP is added
    else:
        pass

    
