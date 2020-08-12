"""
# Ann Marie Burke
# Code for Good - NMFTA
# June - August 2020
# passlist.py -- clear passlist (whitelist),
#                 read in IP addresses from a text file,
#                 passlist all IP addresses from file
"""

import requests
import datetime
import sys
import os.path

PASSLIST_URL = "https://private-anon-ba4b5f3d45-nmftabouncer.apiary-mock.com/v1.1/whitelists"
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
    print("        [filename] - File consisting of IP Addresses to passlist")


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
# Name: removePasslist
# Purpose: remove one entry from passlist
# Input: entry in list, entry type
# Returns: none
"""
def removePasslist(entry, entry_type):
    headers = {
        'Authorization': 'Bearer {access token from /login}'
    }

    if (entry_type == IP):
        entry_id = entry[0]
        remove_url = PASSLIST_URL + "/ipaddresses/" + entry_id + "/delete"
    elif (entry_type == GEO):
        entrySplit = entry.split('#')
        entry_id = entrySplit[0]
        remove_url = PASSLIST_URL + "/geolocations/" + entry_id + "/delete"
    else:
        print("Error message")
        pass
    
    request = requests.delete(remove_url, headers = HEADERS)
    if (not request.status_code == 200):
        print("Error removing entry from passlist.")


"""
# Name: clearPasslist
# Purpose: clears whole passlist
# Input: none
# Returns: none
"""
def clearPasslist():
    allContents = requests.get(PASSLIST_URL, headers=HEADERS)
    if (allContents):
        jsonAllContents = allContents.json()
        ipAddresses = jsonAllContents["IPAddresses"]
        geoLocations = jsonAllContents["GeoLocations"]

        for i in ipAddresses:
            removePasslist(i, IP)

        for i in geoLocations:
            removePasslist(i, GEO)


"""
# Name: passlistAll
# Purpose: passlist all IPs in a list
# Input: list of IP addresses to passlist
# Returns: none
"""
def passlistAll(linesList):
    if (len(linesList) == 0 or linesList == None):
        pass
    else:
        print("Passlisting...\n")
        # TODO: check if valid IP
        ip = ""

        # current time
        start_time = datetime.datetime.utcnow().isoformat()

        # get datetime format from ISO format to be compatible with duration
        datetime_start = datetime.datetime.fromisoformat(str(start_time))

        oneday = datetime.timedelta(hours=24) # duration of passlist is one day
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
            request = requests.post(PASSLIST_URL + "/ipaddresses/create", headers=HEADERS, params=params)
            if (request.status_code == 200):
                print('Success.\n')
            else:
                print('Error.\n')


"""
# Name: main
# Purpose: main function
# Input: none
# Returns: none
# Effects: calls process_args function to process command line arguments
"""
def main():
    clearPasslist()
    filename = process_args()
    if (filename != None):
        linesList = process_file(filename)
        passlistAll(linesList)
    

# call main
main()


"""
# Resources:
#   https://www.w3schools.com/python/python_file_open.asp
#   https://www.guru99.com/reading-and-writing-files-in-python.html
#   https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
#   https://stackoverflow.com/questions/24237524/how-to-split-a-python-string-on-new-line-characters
"""
