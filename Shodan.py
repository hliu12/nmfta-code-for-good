# Andrew Crofts
# Code for Good - NMFTA
# July 2020
# searches Shodan for IP

import shodan

# Name: is_vpn
# Purpose: compares open ports with common ports associated with VPNs
# Input: string representing open port
# Returns: boolean whether IP is a VPN or not
# Effects: none
def is_vpn(port):
    portlist = ["1723", "500", "1701", "1194", ]
    if port in portlist:
        return True
    else:
        return False


# Name: shodan_search
# Purpose: searches for IP address and checks whether it is in the shodan database or not
# Input: string representing IP address
# Returns: boolean whether IP in database or not
# Effects: Prints the information if IP found
def shodan_search(ip):
    try:
        #NOTE: Temporarily using personal Shodan API key
        SHODAN_API_KEY = 'YOUR API KEY HERE'
        api = shodan.Shodan(SHODAN_API_KEY)
        host = api.host(ip)

    # Print general info
        print("""
                IP: {}
             Organization: {}
                Operating System: {}
        """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

        # Print all banners
        vpn = False
        for item in host['data']:
            port = str(item['port'])
            #check if VPN (stops once port associated with VPN detected)
            if (vpn == False):
                vpn = is_vpn(port)
           print("""
                        Port: {}
                        Banner: {}
    
              """.format(item['port'], item['data']))
        return vpn

    except Exception as e:
        print("Clean IP, no match found")
        found = False
        return found

# Name: main
# Purpose: tests shodan search
# Input: none
# Returns: none
# Effects: Prints the information if IP found
def main():
    shodan_search('134.119.189.29')
    print("\n\n\nNew Test....\n\n\n")
    found = shodan_search('144.139.144.217')


main()

