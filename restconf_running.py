import requests
import json
import argparse
import base64
requests.packages.urllib3.disable_warnings()



def set_basic_auth(username, password):
        """this function return a basic-auth header for given username and password"""
        auth = (base64.b64encode((username+":"+password).encode("utf-8"))).decode("utf-8")
        return "Basic {parameters}".format(parameters=auth)



def main():
    parser = argparse.ArgumentParser(description='A simple command-line calculator.')

    parser.add_argument('--ip', type=str, help='IP address of the device')
    parser.add_argument('--username', type=str, help='Username for authentication')
    parser.add_argument('--password', type=str, help='Password for authentication')
    args = parser.parse_args()
    #print(args.ip)
    url = "https://{ip}/restconf/data/Cisco-IOS-XE-native:native/".format(ip=args.ip)
    a=set_basic_auth(username=args.username,password=args.password) 
    headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json',
    'Authorization':a
    }
    response = requests.request("GET", url, headers=headers,verify=False)
    print(response.text)


if __name__ == "__main__":
    main()
#print(response.text)
