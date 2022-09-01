import requests
import json


class Token:
    urlToken = 'https://apiv2.entegrabilisim.com/api/user/token/obtain/'
    accessKey = {"email": "apitestv2@entegrabilisim.com", "password": "apitestv2"}

    def __init__(self):
        pass

    def getToken(self):
        token = requests.request("POST", self.urlToken, data=self.accessKey)
        return token.json()['access']

