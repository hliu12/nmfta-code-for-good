# Tufts Code for Good - NMFTA Bouncer Wrapper
This repository contains a python wrapper for the NMFTA Bouncer API, interacting with the API to incite dynamic responses to threats. 

 ## Wrapper Description
This wrapper was created to diversify the bouncer’s response to threats by inciting dynamic responses. The wrapper contains a variety of responses including ip and geolocation blocking with aspects of randomness and time checking implemented. See Usage for more detail about each response.


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
python3 whitelist.py [filename]
```



## **Installing**

### **Prerequisites**
May require installation of python libraries such as:  
* Requests
* Datetime
* Sys
* Random
* Shodan  

Additionally, requires installation of Debian OS and Apache in order to test Bouncer actions on a server. [see Bouncer instructions for installation under [API Setup/Reference](https://github.com/hliu12/nmfta-code-for-good#api-setupreference).

// move to top?
// link resources for installing these libraries?

### **API Setup/Reference**
This wrapper was made for the NMFTA's open source bouncer API, which contains details on how to set up a local instance of the bouncer API. Installation instructions and documentation can be found at the open 
source repo [here](https://github.com/nmfta-repo/nmfta-bouncer).

## **Testing**

Due to the issues we experienced with setting up a local environment of the bouncer API, test calls were 
done on a mock server of the API. The documentation for this mock server can be found [here](https://nmftabouncer.docs.apiary.io/#).


# **Contributors**
**Ann Marie Burke** (annmarieb1) - *Developer*   
**Henry Liu** (hliu12) - *Developer*  
**Andrew Crofts** (acrofts040) - *Developer*  
**Bobby Wells** - *Dev Lead*  
**Winnona DeSombre** - *Tech Lead*
