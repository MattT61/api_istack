import os
import sys
import requests

# Presume that they pass in the IP address as the parameter

if len(sys.argv) < 2:
    print("Missing parameter: ip-address")
    exit(1)

param = sys.argv[1]

key = os.getenv("IPSTACK_KEY")
if len(key) == 0:
    print("Missing environment variable: IPSTACK_KEY")
    exit(2)

ret = requests.get(f"http://api.ipstack.com/134.201.250.155?access_key={key}")
if "latitude" in ret.json() and "longitude" in ret.json():
    print(str(ret.json()['latitude'])+","+str(ret.json()['longitude']))
else:
    print("Error: Bad return from API call")
    exit(3)

exit(0)