import requests
import json
import urllib3 
from DNAC_auth import DNAC_auth

urllib3.disable_warnings()
def get_sites(token):
    url = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/site'
    headers = {
        'x-auth-token': token,
        'content-type': 'application/json'
    }
    sites = requests.get(url, headers=headers, verify=False).json()
    #print(sites.text)
    sites_dict = json.dumps(sites, indent=2)
    print("****************************************************************")
    print(sites_dict)


if __name__ == "__main__":
    token = DNAC_auth()
    get_sites(token)

