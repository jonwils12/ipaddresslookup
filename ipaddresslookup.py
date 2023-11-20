#imports necessary libraries json for output file and requests for REST
import requests
import json
#testip = 134.201.250.155
#Calls for user input
ip = input("Enter the IP address you would like to lookup: ")
#creates an API call with the user specified IP address
api_url = ("http://api.ipstack.com/%s?access_key=fcfda326dbeea82a06c062150fe1c931&fields=longitude,latitude"%(ip))

#Pulls response from IPSTACK API
response = requests.get(api_url)
#created assignment for output file
answer = response.json()
#displays file in cli 
print(answer)
#answers can be passed to another python tool using from ipaddresslookup import (answer) in the source