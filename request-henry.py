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
    getRequest("show all whitelist contents", "https://private-anon-934f9b5478-nmftabouncer.apiary-mock.com/v1.1/whitelists")
    getRequest("list all whitelist IP addresses", 'https://private-anon-cd74c54b0e-nmftabouncer.apiary-mock.com/v1.1/whitelists/ipaddresses')
    getRequest("list all whitelist geo locations", "https://private-anon-934f9b5478-nmftabouncer.apiary-mock.com/v1.1/whitelists/geolocations")
    getRequest("show all blacklist contents", "https://private-anon-934f9b5478-nmftabouncer.apiary-mock.com/v1.1/blacklists")
    getRequest("list all blacklist IP addresses", "https://private-anon-934f9b5478-nmftabouncer.apiary-mock.com/v1.1/blacklists/ipaddresses")
    getRequest("list all blacklist geo locations", "https://private-anon-934f9b5478-nmftabouncer.apiary-mock.com/v1.1/blacklists/geolocations")
    # Prompts user for IP address
    getRequest("check list membership", "https://private-anon-934f9b5478-nmftabouncer.apiary-mock.com/v1.1/check/" + input("Enter IP address to check for membership: "))


# PURPOSE: Sends a GET request to an API url
# PARAMETERS: A string specifying the type of address, a string url
# RETURN: None
def getRequest(requestType, url): 
    print('\n')
    print("Sending a request to " + requestType + " at: " + url)
    r = requests.get(url)
    print("Status code: " + str(r.status_code))
    print(r.text + '\n')



# calls main function
main()
