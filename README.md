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


## **Installing**

### **Prerequisites**
May require installation of python libraries such as:  
* Requests
* Datetime
* Sys
* Random
* Shodan  

Additionally, requires installation of Debian OS and Apache in order to test Bouncer actions on a server.

### **API Setup/Reference**
This wrapper was made for the NMFTA's open source bouncer API, which contains details on how to set up a
local instance of the bouncer API. Installation instructions and documentation can be found at the open 
source repo [here](https://github.com/nmfta-repo/nmfta-bouncer)

## **Testing**

Due to the issues we experienced with setting up a local environment of the bouncer API, test calls were 
done on a mock server of the API. The documentation for this mock server can be found [here](https://nmftabouncer.docs.apiary.io/#)


# **Contributors**
**Ann Marie Burke** (annmarieb1) - *Developer*   
**Henry Liu** (hliu12) - *Developer*  
**Andrew Crofts** (acrofts040) - *Developer*  
**Bobby Wells** - *Dev Lead*  
**Winnona DeSombre** - *Tech Lead*  
