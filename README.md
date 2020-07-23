# Tufts Code for Good NMFTA Bouncer Wrapper
This repository contains a python wrapper for the NMFTA Bouncer API, interacting with the API to incite dynamic responses to threats. The Python file blacklist.py contains all of the 

 ## Wrapper Description
This wrapper was created to diversify the bouncer’s response to threats by inciting dynamic responses. The wrapper does this by randomly either blocking the geolocation or the IP address of an identified threat for a random time period between 8-24 hours.

## Usage
The functionality of the bouncer may be tested by running blacklist.py in the following manner:

```bash
python blacklist.py [IP Address] [flag]
```

Currently, there are 3 unique flags to choose from:
To run the IP address blocking feature, do:
```bash
python blacklist.py [IP Address] --ip
```
To run the geolocation blocking feature, do:
```bash
python blacklist.py [IP Address] --geo
```
To randomize the response chosen, do: 
```bash
python blacklist.py [IP Address] --random
```


### **Prerequisites**
May require installation of python libraries such as:
Requests
Datetime
Sys
Random
Shodan

	Additionally, requires installation of Debian OS and Apache in order to test Bouncer actions on a server.

### **Installing**





# **Contributors**
**Ann Marie Burke** - *Developer* - annmarieb1
**Henry Liu** - *Developer* - hliu12
**Andrew Crofts** - *Developer* - acrofts040
**Bobby Wells** - *Dev Lead* 
**Winnona DeSombre** - *Tech Lead*
