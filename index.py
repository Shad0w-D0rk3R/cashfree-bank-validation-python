'''
Below is an integration flow on how to use Cashfree's bank validation.
Please go through the payout docs here: https://docs.cashfree.com/docs/payout/guide/

The following script contains the following functionalities :
    1.getToken() -> to get auth token to be used in all following calls.
    2.verifyBankAccount() -> to verify bank account.


All the data used by the script can be found in the config.ini file. This includes the clientId, clientSecret, bankDetails section.
You can change keep changing the values in the config file and running the script.
Please enter your clientId and clientSecret, along with the appropriate enviornment and bank details
'''


#warning the following code is written for python2 and tested using python2.7
#warning the following code has a dependency on the request, configparser library

import configparser
import requests
import json

#read the config file
config = configparser.ConfigParser()
config.optionxform = str
if config.read('config.ini') == []:
    print 'unable to read config'
    exit()

#default
default = config._sections['default']
clientId, clientSecret, env = default['clientId'], default['clientSecret'], default['env']
baseurl = config._sections['baseUrl'][env]
url = config._sections['url']

#get auth token
def getToken():
    try:
        finalUrl = baseurl + url['auth']
        r =  requests.post(finalUrl, headers={"X-Client-Id":clientId, "X-Client-Secret":clientSecret})

        if (not r):
            raise Exception("response err: response is null")

        content = json.loads(r.content)


        if (content['status'] != "SUCCESS") or (content['subCode'] != "200"):
            raise Exception("response err: response is incorrect \n" + content["message"])
        return content["data"]["token"]
    except Exception as err:
        print 'err in getting token'
        raise Exception(err)


#verify bank account details
def verifyBankAccount(token):
    try:
        bankDetails = config._sections['bankDetails']
        queryString = "?"
        for k,v in bankDetails.items():
            queryString += k + "=" + v + "&"
        finalUrl = baseurl + url['bankValidation'] + queryString[:-1]
        r = requests.get(finalUrl, headers={"X-Client-Id":clientId, "X-Client-Secret":clientSecret, 'Content-Type': 'application/json','Authorization': 'Bearer ' + token})
        content = json.loads(r.content)

        if (content['status'] != "SUCCESS") or (content['subCode'] != "200"):
            raise Exception("response err: response is incorrect \n" + content["message"])
        
        print json.dumps(content)
    except Exception as err:
        print 'err in verifying bank account'
        raise Exception(err)

'''
The flow executed below is:
1. fetching the auth token
2. verifying bank account
'''

#main execution loop
if __name__ =="__main__":
    token = getToken()
    verifyBankAccount(token)

