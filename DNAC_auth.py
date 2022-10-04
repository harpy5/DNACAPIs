import requests
import json
import urllib3 

urllib3.disable_warnings()
def DNAC_auth():
    url = 'https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token'
    username= 'dnacdev'
    password = 'D3v93T@wK!'

    headers = {
        'content-type': "application/json",
    }

    response = requests.post(url, auth=(username, password), verify=False, headers=headers)
    #print(response.text)
    response_dict= json.loads(response.text)
    token = response_dict['Token'] 
    #print('**************************************')
    #print(token)
    return token

if __name__ == "__main__":
    DNAC_auth()
