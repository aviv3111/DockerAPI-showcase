from flask import Flask
from flask import request
import base64
import requests
import json

def set_basic_auth(username, password):
        """this function return a basic-auth header for given username and password"""
        auth = (base64.b64encode((username+":"+password).encode("utf-8"))).decode("utf-8")
        return "Basic {parameters}".format(parameters=auth)

app =  Flask(__name__)

@app.route("/", methods=["GET"])
def route():
    return "app is working!"

@app.route("/backup", methods=["GET"])
def backup():
    ipadd = request.args.get("ip")
    user = request.args.get("user")
    pas = request.args.get("pass")
    auth = set_basic_auth(username=user, password=pas)
    headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json',
    'Authorization':auth
    }
    url = "https://{ip}/restconf/data/Cisco-IOS-XE-native:native/".format(ip=ipadd)
    response = requests.request("GET", url, headers=headers,verify=False)
    return response.json()

@app.route("/changename", methods=["GET"])
def changename():
    ipadd = request.args.get("ip")
    user = request.args.get("user")
    pas = request.args.get("pass")
    hostname= request.args.get("name")
    auth = set_basic_auth(username=user, password=pas)
    headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json',
    'Authorization':auth
    }
    payload = json.dumps({
        "Cisco-IOS-XE-native:hostname":hostname})
    url = "https://{ip}/restconf/data/Cisco-IOS-XE-native:native/hostname/".format(ip=ipadd)

    requests.request("PUT", url, headers=headers, data=payload,verify=False)

    return "done!"



if __name__ == "__main__":
    app.run(host="0.0.0.0")