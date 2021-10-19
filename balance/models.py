import sqlite3
import requests
from requests.sessions import Session
import json
from config import APIKEY, URL


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

    def consultaSQL2(self, consulta,params):
        conn = sqlite3.connect(self.RUTA_DDBB)

        cur = conn.cursor()
        cur.execute(consulta,params)
        
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
    
    def modificaSQL(self, consulta, params):
        conn = sqlite3.connect(self.RUTA_DDBB)

        cur = conn.cursor()

        cur.execute(consulta, params)
        conn.commit()
        conn.close()

class APIError(Exception):
    pass

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
    
