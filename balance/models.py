import sqlite3
import requests


APIKEY = "05915253-A982-431B-87AA-55C645B31B41"
URL = "https://rest.coinapi.io/v1/exchangerate/{}/{}"

class APIError(Exception):
    pass

class DDBBmanager():
    def __init__(self, RUTA_DDBB):
        self.RUTA_DDBB = RUTA_DDBB

    def consultaSQL(self, consulta):
        conn = sqlite3.connect(self.RUTA_DDBB)

        cur = conn.cursor()
        cur.execute(consulta)
        
        keys = []
        for item in cur.description:
            keys.append(item[0])

        compras = []
        for registro in cur.fetchall():
            ix_clave = 0
            dic = {}
            for columna in keys:
                dic[columna] = registro[ix_clave]
                ix_clave += 1
            compras.append(dic)

        conn.close()
        return compras

class CriptoValueModel():
    def __init__(self,inicio,fin):
        self.de = inicio
        self.a = fin
        self.valor = 0.0

    def obtener(self):
        cabecera = {"X-CoinAPI-Key": APIKEY}
        respuesta = requests.get(URL.format(self.de, self.a), headers=cabecera)

        if respuesta.status_code == 200:
            self.valor = respuesta.json()["rate"]
        else:
            print(respuesta.json())
            raise APIError(f"Se ha producido el error {respuesta.status_code} en la peticion")
    

class ConversorMoneda():
    diccionario = {
        'Euro (€)' : 'EUR', 
        'Bitcoin (BTC)' : "BTC", 
        'Ethereum (ETH)': 'ETH', 
        'Ripple (XRP)':'XRP', 
        'Litecoin (LTC)': 'LTC',
        'Bitcoin Cash (BCH)':'BCH', 
        'Binance (BNB)':'BNB', 
        'Tether (USDT)':'USDT', 
        'EOS (EOS)':'EOS', 
        'Bitcoin SV (BSV)':'BSV', 
        'Stellar Lumens (XLM)':'XLM', 
        'Cardano (ADA)':'ADA', 
        'Tronix (TRX)':'TRX', 
    }

    def __init__(self) -> None:
        pass

    def convertirStringMoneda(self,de):
        return self.diccionario[de]