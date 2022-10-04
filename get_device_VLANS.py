import requests
import json
import urllib3 
from DNAC_auth import DNAC_auth
from get_devices import get_devices
from get_device_ID import get_device_ID

urllib3.disable_warnings()
def get_vlans(token, id):
    url = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device/{}/vlan'.format(id)
    headers = {
        'x-auth-token': token,
        'content-type': 'application/json'
    }
    vlans = requests.get(url, headers=headers, verify=False)
    #print(sites.text)
    vlans_dict = json.loads(vlans.text)
    #print("****************************************************************")
    print(json.dumps(vlans_dict, indent=2))
    #return vlans_dict


if __name__ == "__main__":
    token = DNAC_auth()
    devices = get_devices(token)
    id = get_device_ID(devices, device_name='leaf2.test.com')
    get_vlans(token, id)