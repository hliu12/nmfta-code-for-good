# Tufts Code for Good - NMFTA Bouncer Wrapper
This repository contains a python wrapper for the [NMFTA Bouncer API][NMFTA Bouncer], interacting with the API to incite dynamic responses to threats. 


## Wrapper Description
This wrapper was created to showcase what a dynamic security environment can look like. Our scripts diversify the bouncer’s response to threats by inciting dynamic responses. The wrapper contains a variety of responses including ip and geolocation blocking with aspects of randomness and time checking implemented. See [Usage](#Usage) for more detail about each response. All calls are made to the API’s [mock server](https://nmftabouncer.docs.apiary.io/#), so it has not been thoroughly tested. If you would like to use this as a starting point, we recommend you create a local instance of the server and replace calls to the mock server with calls to the local server.

## A Note on Terminology
We are aware of the implications the terms "blacklist" and "whitelist" have. Therefore, we will be using the terms "blocklist" and "passlist," joining Linux kernel and GitHub [article linked](https://thenextweb.com/dd/2020/07/13/linux-kernel-will-no-longer-use-terms-blacklist-and-slave/#:~:text=Alternatives%20for%20blacklist%2Fwhitelist%20are,the%20right%20way%20to%20go), among others, in their efforts to transition away from these terms towards inclusive terms.


## Usage

### Blocklist.py
This script implements a dynamic response by randomly either blocking the geolocation or the IP address of an identified threat for a random time period between 8-24 hours.  
Currently, there are 3 unique flags to choose from: --ip, --geo, and --random. The script will activate the response indicated by the flag, or for the random flag, choose a response randomly.  
The functionality of the script may be tested by running:
```bash
python3 blocklist.py [flag] [IP Address]
```

### Timezone_geoblock.py
This script checks if a user at a given IP address is attempting to connect at a reasonable time of day for the geolocation of the IP address, namely between 7 a.m. and 10 p.m. If the user is not attempting to gain access within reasonable working hours for their geolocation, this script blocks the geolocation of the given IP address until the next reasonable time window (7 a.m. the next day).  
The functionality of the script may be tested by running:
```bash
python3 timezone_geoblock.py [IP Address]
```

### Passlist.py
This script passlists known good IP addresses for a day. It takes in a text file of IP addresses on the command line (each IP must be on a new line), reads in the IP addresses, clears the current passlist, and passlists all IP addresses from the given file. It is attended to run once every day so that the passlist is updated, ensuring that only trusted users have guaranteed access.  
The functionality of the script may be tested by running:
```bash
python3 passlist.py [filename]
```

### Shodan.py
This script searches a given IP on the Shodan search engine through the Shodan API. Through this it analyzes which ports are open and determines whether the given IP is a VPN. If it is, it returns a boolean of true, and will be blocklisted through Bouncer.  
The functionality of the script may be tested by running:
```bash
python3 Shodan.py
```


## **Installing**

### **Prerequisites**
Requires installation of python libraries such as:  
* [requests](https://pypi.org/project/requests/2.7.0/) (documentation [here](https://requests.readthedocs.io/en/master/)) - required for `blocklist.py`, `timezone_geoblock.py`, `passlist.py`

* [datetime](https://docs.python.org/3/library/datetime.html) - required for `blocklist.py`, `timezone_geoblock.py`, `passlist.py`

* [sys](https://docs.python.org/3/library/sys.html) - required for `blocklist.py`, `Shodan.py`, `timezone_geoblock.py`, `passlist.py`
* [random](https://docs.python.org/3/library/random.html) - required for `blocklist.py`, `timezone_geoblock.py`, `passlist.py`
* [shodan](https://shodan.readthedocs.io/en/latest/)  - required for `Shodan.py`

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