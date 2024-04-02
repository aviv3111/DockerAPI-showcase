import requests
import json

url = "https://192.168.199.130/restconf/data/Cisco-IOS-XE-native:native/hostname/"
username=(input(" enter a string "))
payload = json.dumps({
  "Cisco-IOS-XE-native:hostname":username
})
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic YWRtaW46YWRtaW4xMjM='
}

response = requests.request("PUT", url, headers=headers, data=payload,verify=False)

print((response[0]))