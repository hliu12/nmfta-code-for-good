# Tufts Code for Good - NMFTA Bouncer Wrapper
This repository contains a python wrapper for the [NMFTA Bouncer API][NMFTA Bouncer], interacting with the API to incite dynamic responses to threats. 


## Wrapper Description
This wrapper was created to showcase what a dynamic security environment can look like. Our scripts diversify the bouncer’s response to threats by inciting dynamic responses. The wrapper contains a variety of responses including ip and geolocation blocking with aspects of randomness and time checking implemented. See [Usage](#Usage) for more detail about each response. All calls are made to the API’s [mock server](https://nmftabouncer.docs.apiary.io/#), so it has not been thoroughly tested. If you would like to use this as a starting point, we recommend you create a local instance of the server and replace calls to the mock server with calls to the local server.


## Usage

### Blacklist.py
This script implements a dynamic response by randomly either blocking the geolocation or the IP address of an identified threat for a random time period between 8-24 hours.  
Currently, there are 3 unique flags to choose from: --ip, --geo, and --random. The script will activate the response indicated by the flag, or for the random flag, choose a response randomly.
The functionality of the script may be tested by running:
```bash
python3 blacklist.py [flag] [IP Address]
```

### Timezone_geoblock.py
This script checks that a user at a given IP address is attempting to connect at a reasonable time of day (7AM - 10PM). If the user's geolocation is not within this time frame, this script blocks the geolocation of the given IP address until the reasonable time window.

The functionality of the script may be tested by running:
```bash
python3 timezone_geoblock.py [IP Address]
```

### Whitelist.py
This script whitelists known good IP addresses for a day. It takes in a text file of IP addresses on the command line (each IP must be on a new line), reads in the IP addresses, clears the current whitelist, and whitelists all IP addresses from the given file.
The functionality of the script may be tested by running:
```bash
python3 whitelist.py [filename]
```

### Shodan.py
This script searches a given IP on the Shodan search engine through the Shodan API. Through this it analyzes which ports are open and determines whether the given IP is a VPN. If it is, it returns a boolean of true, and will be blacklisted through Bouncer. 
The functionality of the script may be tested by running:
```bash
python3 Shodan.py
```


## **Installing**

### **Prerequisites**
May require installation of python libraries such as:  
* [Requests](https://pypi.org/project/requests/2.7.0/) (documentation [here](https://requests.readthedocs.io/en/master/)) - required for `blacklist.py`, `timezone_geoblock.py`, `whitelist.py`
 * Install by running
`pip install requests` or `pipenv install requests`

* [Requests](https://pypi.org/project/requests/2.7.0/) ([documentation](https://requests.readthedocs.io/en/master/)) - required for `blacklist.py`, `timezone_geoblock.py`, `whitelist.py`
``
pip install requests
``
or
``
pipenv install requests
``

* Datetime - required for `blacklist.py`, `timezone_geoblock.py`, `whitelist.py`

* Sys - required for `blacklist.py`, `Shodan.py`, `timezone_geoblock.py`, `whitelist.py`
* Random - required for `blacklist.py`, `timezone_geoblock.py`, `whitelist.py`
* Shodan  - required for `Shodan.py`

Additionally, requires installation of Debian OS and Apache in order to test Bouncer actions on a server. [see Bouncer instructions for installation under [API Setup/Reference](#api-setupreference).

### **API Setup/Reference**
This wrapper was made for the NMFTA's open source bouncer API, which contains details on how to set up a local instance of the bouncer API. Installation instructions and documentation can be found at the open 
source repo [here][NMFTA Bouncer].


# **Contributors**
**Ann Marie Burke** (annmarieb1) - *Developer*   
**Henry Liu** (hliu12) - *Developer*  
**Andrew Crofts** (acrofts040) - *Developer*  
**Bobby Wells** - *Dev Lead*  
**Winnona DeSombre** - *Tech Lead*

<!-- Links -->
[NMFTA Bouncer]: https://github.com/nmfta-repo/nmfta-bouncer