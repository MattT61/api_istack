#
# fetch_ip
# A simple script to return the latitude and longitude of a given IP address
#
# Input:
# ip-address : parameter to the script
# access_key : Environment variable for the IPStack API
#
# Output:
# If no error, output is latitude, longitude to the console
# If there is an error, output is the error string and error code is set to indicate a problem
#
# Notes:
# The requests library is the typical manner of fetching REST APi data. The requirements of the
# project specified not using a third-party library. As such, the request() function is used instead.
# I believe this code came from the Internet some years back, I've used it in numerous projects.

import os
import sys
from Response import request

# Presume that they pass in the IP address as the parameter

if len(sys.argv) < 2:
    print("Missing parameter: ip-address")
    exit(1)

# Make sure it is valid
param = sys.argv[1]

# Get the api key from the environment as documented.

key = os.getenv("IPSTACK_KEY")
if len(key) == 0:
    print("Missing environment variable: IPSTACK_KEY")
    exit(2)

# Build an API call to ipstack, which will be of the form <url>/<ip-to-fetch>?access_key=<key?
url = f"http://api.ipstack.com/{param}?access_key={key}"

ret = request(url)
if "latitude" in ret.json() and "longitude" in ret.json():
    print(str(ret.json()['latitude'])+","+str(ret.json()['longitude']))
else:
    print("Error: Bad return from API call")
    exit(3)

exit(0)
