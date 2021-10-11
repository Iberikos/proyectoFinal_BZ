import requests
from . import APIKEY, URL

class APIError(Exception):
    pass

class CriptoValueModel():
    def __init__(self):
        self.de = ""
        self.a = ""
        self.valor = 0.0

    def obtener(self):
        cabecera = {"X-CoinAPI-Key": APIKEY}
        respuesta = requests.get(URL.format(self.de, self.a), headers=cabecera)

        if respuesta.status_code == 200:
            self.valor = respuesta.json()["rate"]
        else:
            print(respuesta.json())
            raise APIError(f"Se ha producido el error {respuesta.status_code} en la peticion")
            