import requests
from AllToken.Token.Tokens import Token


class Product:
    urlProducts = 'https://apiv2.entegrabilisim.com/product/page=1/'
    token = Token()

    def __init__(self):
        pass

    def getProducts(self):
        payload = {}
        y = self.token.getToken()
        Aut = 'JWT ' + y
        headers = {'Authorization': Aut,
                   'Content-Type': 'application/json'}
        response = requests.request("GET", self.urlProducts, headers=headers, data=payload)
        return response.json().get('porductList')


