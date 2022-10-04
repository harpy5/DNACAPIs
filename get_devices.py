import requests
import json
import urllib3 
from DNAC_auth import DNAC_auth

urllib3.disable_warnings()
def get_devices(token):
    url = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device'
    headers = {
        'x-auth-token': token,
        'content-type': 'application/json'
    }
    devices = requests.get(url, headers=headers, verify=False)
    #print(sites.text)
    devices_dict = json.loads(devices.text)
    #print("****************************************************************")
    #print(devices_dict)
    return devices_dict


if __name__ == "__main__":
    token = DNAC_auth()
    get_devices(token)