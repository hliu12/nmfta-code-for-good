# Ann Marie Burke
# Code for Good - NMFTA
# June 2020
# request-annmarie.py - sends GET requests to Bouncer API
#
# Note: a problem I am seeing with Search is that the response always has a
# status code of 200 and a status of success for any IP I search for

import requests

# Name: list_print
# Purpose: function for printing List request
# Input: json-formatted response, string of the attribute of the entry (IP, Geo)
# Returns: none
# Effects: prints information from request response
def list_print(jsonResponse, attribute):
	if attribute == "all":
		print("IP Addresses: " + str(jsonResponse["IPAddresses"]))
		print("GeoLocations: " + str(jsonResponse["GeoLocations"]))
	elif attribute == "ip":
		print("IP Addresses: " + str(jsonResponse["IPAddresses"]))
	elif attribute == "geo":
		print("GeoLocations: " + str(jsonResponse["GeoLocations"]))
	else:
		pass

# Name: search_print
# Purpose: function for printing Search request
# Input: json-formatted response, string of the attribute of the entry (IP, Geo)
# Returns: none
# Effects: prints information from request response
def search_print(jsonResponse, attribute):
	# print(str(jsonResponse)) # prints json response
	if attribute == "ip":
		print("Input IP: " + str(jsonResponse["SearchResult"]["Input_IP"]))
		print("Entries: " + str(jsonResponse["SearchResult"]["Entries"]))
	# elif attribute == "geo":
	# 	print("GeoLocations: " + str(jsonResponse["GeoLocations"]))
	else:
		pass

# Name: detail_print
# Purpose: function for printing Get Details request
# Input: json-formatted response
# Returns: none
# Effects: prints information from request response
def detail_print(jsonResponse):
	# print(str(jsonResponse)) # prints json response
	print("Entry: " + str(jsonResponse["Entry"]))

# Name: get_request
# Purpose: function for sending request and printing
# Input: string representing what the request is to
#		 string of the attribute of the entry (IP, Geo)
# 		 string of format of request
# 		 string of url
# Returns: none
# Effects: Prints what you are requesting, url, status code and text
# Note: print call for header, headers content type, and text are commented out
def get_request(what, attribute, format, url):
	# set the headers of the request
	headers = {
  		'Authorization': 'Bearer {access token from /login}'
	}

	# print stuff
	print('\n')
	print('----- Sending request to ' + what + ' -----')
	print(url)
	response = requests.get(url, headers=headers)


	print('Status code: ' + str(response.status_code)) # print status code
	# print('Headers: ' + str(response.headers)) # print headers
	print('\n')

	# headers returns a dictionary-like object,
	# so here is an example of accessing value with key 'Content-Type'
	# print('Headers[Content-Type]: ' + str(response.headers['Content-Type']))

	# print('Text: \n' + response.text + '\n')

	if response:
		jsonResponse = response.json() # returns dictionary --> access values using key
		print("Status: " + str(jsonResponse["Result"]["Status"]))

		if format == "list": # if getting list of items
			list_print(jsonResponse, attribute)
		elif format == "search": # if searching for item using IP
			search_print(jsonResponse, attribute)
		elif format == "details": # if getting details of item using entry ID
			detail_print(jsonResponse)
	else:
		print("Status code is false (not between 200 and 400)")
		# reference: https://realpython.com/python-requests/#status-codes

	print('\n')


# Name: main
# Purpose: main function
# Input: none
# Returns: none
# Effects: calls get_request_format function
# Note: only shows examples of calls, does not make all possible calls to API
def main():
	# List
	# get_request("Whitelist: All Contents", "all", "list", 
	# 	"https://private-anon-cd74c54b0e-nmftabouncer.apiary-mock.com/v1.1/whitelists")
	# get_request("Whitelist: IP Addresses - List", "ip", "list", 
	# 	"https://private-anon-cd74c54b0e-nmftabouncer.apiary-mock.com/v1.1/whitelists/ipaddresses")
	# get_request("Whitelist: Geo Locations - List", "geo", "list", 
	# 	"https://private-anon-2fd025e551-nmftabouncer.apiary-mock.com/v1.1/whitelists/geolocations")
	# get_request("Blacklist: All Contents", "all", "list", 
	# 	"https://private-anon-cd74c54b0e-nmftabouncer.apiary-mock.com/v1.1/blacklists")
	# get_request("Blacklist: IP Addresses - List", "ip", "list", 
	# 	"https://private-anon-86ddcc4f98-nmftabouncer.apiary-mock.com/v1.1/blacklists/ipaddresses")
	# get_request("Blacklist: Geo Locations - List", "geo", "list", 
	# 	"https://private-anon-86ddcc4f98-nmftabouncer.apiary-mock.com/v1.1/blacklists/geolocations")


	# Search
	#
	# Note: a problem I am seeing with Search is that the response always has a
	# status code of 200 and a status of success for any IP I search for
	get_request("Whitelist: IP Addresses \n    Search 192.168.100.0, 192.168.101.0", "ip", "search", 
		"http://private-anon-86ddcc4f98-nmftabouncer.apiary-mock.com/v1.1/whitelists/ipaddresses/filter/192.168.100.0%2B24%2C192.168.101.0%2B24")

	get_request("Blacklist: IP Addresses \n    Search 192.168.100.0, 192.168.101.0", "ip", "search",
		"https://private-anon-86ddcc4f98-nmftabouncer.apiary-mock.com/v1.1/blacklists/ipaddresses/filter/192.168.100.0%2B24%2C192.168.101.0%2B24")

	get_request("Blacklist: IP Addresses \n    Search 127.0.0.1, 127.0.1.0", "ip", "search",
		"https://private-anon-86ddcc4f98-nmftabouncer.apiary-mock.com/v1.1/blacklists/ipaddresses/filter/127.0.0.1%2B24%2C127.0.1.0%2B24")

	get_request("Whitelist: IP Addresses \n    Search 192.168.100.14", "ip", "search",
		"https://private-anon-86ddcc4f98-nmftabouncer.apiary-mock.com/v1.1/whitelists/ipaddresses/filter/192.168.100.14%2B24")

	get_request("Whitelist: IP Addresses \n    Search 127.0.0.1", "ip", "search",
		"https://private-anon-86ddcc4f98-nmftabouncer.apiary-mock.com/v1.1/whitelists/ipaddresses/filter/127.0.0.1%2B24")

	get_request("Whitelist: IP Addresses \n    Search 8.8.4.4, 8.8.8.8", "ip", "search",
		"https://private-anon-86ddcc4f98-nmftabouncer.apiary-mock.com/v1.1/whitelists/ipaddresses/filter/8.8.4.4%2B24%2C8.8.8.8%2B24")
	

	# Get Details
	# get_request("Whitelist: Get Details of Entry 884d9804999fc47a3c2694e49ad2536a", "ip", "details", 
	# 	"https://private-anon-604624fc1d-nmftabouncer.apiary-mock.com/v1.1/whitelists/ipaddresses/884d9804999fc47a3c2694e49ad2536a")
	
	# get_request("Blacklist: Get Details of Entry 884d9804999fc47a3c2694e49ad2536a", "ip", "details", 
	# 	"https://private-anon-86ddcc4f98-nmftabouncer.apiary-mock.com/v1.1/blacklists/ipaddresses/884d9804999fc47a3c2694e49ad2536a")
	
	# get_request("Blacklist: Get Details of Entry 884d9804999fc47a3c2694e49ad2536a", "geo", "details", 
	# 	"https://private-anon-86ddcc4f98-nmftabouncer.apiary-mock.com/v1.1/blacklists/geolocations/884d9804999fc47a3c2694e49ad2536a")
	


# call main
main()



# References:
#    https://requests.readthedocs.io/en/master/user/quickstart/
#    https://requests.readthedocs.io/en/master/

# Important links:
#    https://github.com/nmfta-repo/nmfta-bouncer/blob/master/apiary.apib
#    https://nmftabouncer.docs.apiary.io/