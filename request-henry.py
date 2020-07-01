# Code for Good - NMFTA
#
# request-henry.py
# Bouncer API Get Request testing
#
# Written by Henry Liu
#       on June 2020

import requests

# PURPOSE: Main function
# PARAMETERS: None
# RETURN: None
def main():
    # getRequest("show all whitelist contents", "https://private-anon-934f9b5478-nmftabouncer.apiary-mock.com/v1.1/whitelists")
    # getRequest("search", "https://private-anon-934f9b5478-nmftabouncer.apiary-mock.com/v1.1/whitelists/ipaddresses/filter/192.168.100.0+24,192.168.101.0+24")
    # getRequest("list all whitelist IP addresses", 'https://private-anon-cd74c54b0e-nmftabouncer.apiary-mock.com/v1.1/whitelists/ipaddresses')
    # getRequest("list all whitelist geo locations", "https://private-anon-934f9b5478-nmftabouncer.apiary-mock.com/v1.1/whitelists/geolocations")
    # getRequest("show all blacklist contents", "https://private-anon-934f9b5478-nmftabouncer.apiary-mock.com/v1.1/blacklists")
    # getRequest("list all blacklist IP addresses", "https://private-anon-934f9b5478-nmftabouncer.apiary-mock.com/v1.1/blacklists/ipaddresses")
    # getRequest("list all blacklist geo locations", "https://private-anon-934f9b5478-nmftabouncer.apiary-mock.com/v1.1/blacklists/geolocations")
    # getRequest("get details from blacklist ip", "https://private-anon-f6b8e6d09a-nmftabouncer.apiary-mock.com/v1.1/blacklists/ipaddresses/884d9804999fc47a3c2694e49ad2536a ")
    # Prompts user for IP address
    # getRequest("check list membership", "https://private-anon-934f9b5478-nmftabouncer.apiary-mock.com/v1.1/check/" + input("Enter IP address to check for membership: "))
    
    # Testing Get Details function
    getDetails("884d9804999fc47a3c2694e49ad2536a", "blacklists")
    getDetails("88888", "whitelists")
    # Gibberish input results in same output
    getDetails("gibberish", "blacklists")


# PURPOSE: Sends a GET request to an API url
# PARAMETERS: A string specifying the type of address, a string url
# RETURN: None
def getRequest(requestType, url): 
    print('\n')
    print("Sending a request to " + requestType + " at: " + url)
    r = requests.get(url)
    print("Status code: " + str(r.status_code))
    print(r.text + '\n')


# PURPOSE: Sends a GET request to get details of an IP address from either the whitelist or blacklist
# PARAMETERS: A string IP address, a string specifying the list
# RETURN: None
def getDetails(ipAddress, listName): 
    url = "https://private-anon-f6b8e6d09a-nmftabouncer.apiary-mock.com/v1.1/" + listName + "/ipaddresses/" + ipAddress
    print('\n')
    print("Searching for IP address: " + ipAddress + " at: " + url)
    r = requests.get(url)
    print("Status code: " + str(r.status_code))
    print(r.text + '\n')



# calls main function
main()
