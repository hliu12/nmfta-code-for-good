"""
# Ann Marie Burke
# Code for Good - NMFTA
# July 2020
# whitelist.py -- clear whitelist,
#                 read in IP addresses from a text file,
#                 whitelist all IP addresses from file
"""

import requests
import datetime
import sys
import os.path

WHITELIST_URL = "https://private-anon-ba4b5f3d45-nmftabouncer.apiary-mock.com/v1.1/whitelists"
IP = "ip"
GEO = "geo"
HEADERS = {
    'Authorization': 'Bearer {access token from /login}'
}

"""
# Name: print_usage
# Purpose: print usage for script
# Input: none
# Returns: none
"""
def print_usage():
    print(f"Usage: python3 {sys.argv[0]} [filename]")
    print("        [filename] - File consisting of IP Addresses to whitelist")


"""
# Name: process_args
# Purpose: process command line arguments
# Input: none
# Returns: if 2 args passed, returns filename
#          else, returns None
"""
def process_args():
    args = sys.argv # get args
    argc = len(args) # get num of args

    if (argc == 2):
        return args[1]
    else:
        print_usage()
        return None


"""
# Name: process_args
# Purpose: open file passed in, load all lines into a string, close file,
#          convert string into list of lines
# Input: name of file
# Returns: list of all lines in text file
"""
def process_file(filename):
    if (filename != None):
        print("Reading from file: " + filename + '\n')
        # f = open(filename, "rt")

        if (os.path.isfile(filename)):
            with open(filename) as f:
                file_txt = f.read()

            if (not f.closed):
                f.close()

            linesList = file_txt.splitlines()

            return linesList
        else:
            print("No file found")
            return []
    else:
        return []


"""
# Name: removeWhitelist
# Purpose: remove one entry from whitelist
# Input: entry in list, entry type
# Returns: none
"""
def removeWhitelist(entry, entry_type):
    headers = {
        'Authorization': 'Bearer {access token from /login}'
    }

    if (entry_type == IP):
        # print("---remove IP---")
        entry_id = entry[0]
        remove_url = WHITELIST_URL + "/ipaddresses/" + entry_id + "/delete"
        # print(remove_ip_url)
    elif (entry_type == GEO):
        # print("---remove Geo---")
        entrySplit = entry.split('#')
        entry_id = entrySplit[0]
        remove_url = WHITELIST_URL + "/geolocations/" + entry_id + "/delete"
        # print(remove_geo_url)
    else:
        print("Error message")
        pass
    
    request = requests.delete(remove_url, headers = HEADERS)
    if (not request.status_code == 200):
        print("Error removing entry from whitelist.")


"""
# Name: clearWhitelist
# Purpose: clears whole whitelist
# Input: none
# Returns: none
"""
def clearWhitelist():
    allContents = requests.get(WHITELIST_URL, headers=HEADERS)
    if (allContents):
        jsonAllContents = allContents.json()
        ipAddresses = jsonAllContents["IPAddresses"]
        geoLocations = jsonAllContents["GeoLocations"]

        for i in ipAddresses:
            removeWhitelist(i, IP)

        for i in geoLocations:
            removeWhitelist(i, GEO)


"""
# Name: whitelistAll
# Purpose: whitelist all IPs in a list
# Input: list of IP addresses to whitelist
# Returns: none
"""
def whitelistAll(linesList):
    if (len(linesList) == 0 or linesList == None):
        pass
    else:
        print("Whitelisting...\n")
        # TODO: check if valid IP
        ip = ""

        # current time
        start_time = datetime.datetime.utcnow().isoformat()

        # get datetime format from ISO format to be compatible with duration
        datetime_start = datetime.datetime.fromisoformat(str(start_time))

        oneday = datetime.timedelta(hours=24) # duration of whitelist is one day
        # print("Duration of block: " + str(oneday))
        
        the_end = datetime_start + oneday
        end_time = the_end.isoformat() # convert to ISO format

        params = {
            "IP": ip,
            "Start_Date": start_time,
            "End_Date" : end_time,
        }

        for i in linesList:
            ip = i
            print(ip)
            request = requests.post(WHITELIST_URL + "/ipaddresses/create", headers=HEADERS, params=params)
            print('Status code: ' + str(request.status_code))
            print('\n')


"""
# Name: main
# Purpose: main function
# Input: none
# Returns: none
# Effects: calls process_args function to process command line arguments
"""
def main():
    clearWhitelist()
    filename = process_args()
    if (filename != None):
        linesList = process_file(filename)
        whitelistAll(linesList)
    

# call main
main()


"""
# Resources:
#   https://www.w3schools.com/python/python_file_open.asp
#   https://www.guru99.com/reading-and-writing-files-in-python.html
#   https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
#   https://stackoverflow.com/questions/24237524/how-to-split-a-python-string-on-new-line-characters
"""