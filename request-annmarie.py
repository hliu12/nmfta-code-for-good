# Ann Marie Burke
# Code for Good - NMFTA
# June 2020
# sends GET request to Bouncer API


import requests

# Name: get_request_format
# Purpose: function for sending request and printing
# Input: string representing what the request is to, string of url
# Returns: none
# Effects: Prints what you are requesting, url, status code and text returned
def get_request_format(what, url):
	print('\n')
	print('----- Sending request to ' + what + ' -----')
	print(url)
	r = requests.get(url)
	print('Status code: ' + str(r.status_code))
	print('Text: \n' + r.text + '\n')

# Name: main
# Purpose: main function
# Input: none
# Returns: none
# Effects: calls get_request_format function
def main():
	get_request_format('whitelist',
		'https://private-anon-cd74c54b0e-nmftabouncer.apiary-mock.com/v1.1/whitelists')
	get_request_format('white list IPs',
		'https://private-anon-cd74c54b0e-nmftabouncer.apiary-mock.com/v1.1/whitelists/ipaddresses')
	get_request_format('blacklist', 'https://private-anon-cd74c54b0e-nmftabouncer.apiary-mock.com/v1.1/blacklists')


# call main
main()



# References:
#    https://requests.readthedocs.io/en/master/user/quickstart/
#    https://requests.readthedocs.io/en/master/

# Important links:
#    https://github.com/nmfta-repo/nmfta-bouncer/blob/master/apiary.apib
#    https://nmftabouncer.docs.apiary.io/