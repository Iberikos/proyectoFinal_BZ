import sqlite3
import requests
from requests.sessions import Session
import json
from config import APIKEY, URL, URLTOTAL
from balance.forms import Coins

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

    def consultaSQL2(self, consulta, params):
        conn = sqlite3.connect(self.RUTA_DDBB)

        cur = conn.cursor()
        cur.execute(consulta, params)
        
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
            raise APIError(f"Se ha producido el error {respuesta.status_code} en la peticion")
    
class StatusModel():

    def __init__(self,based):
        self.based = based
        self.spent = 0.0
        self.currentValue = 0.0

    def calcular(self):
        consulta = "SELECT SUM(cantFrom) FROM compras WHERE coinFrom='EUR'"
        sumFrom = self.based.consultaSQL(consulta)
        consulta = "SELECT SUM(cantTo) FROM compras WHERE coinTo='EUR'"
        sumTo = self.based.consultaSQL(consulta)
        if sumFrom[0]['SUM(cantFrom)']==None:
            sumFrom[0]['SUM(cantFrom)']=0
        if sumTo[0]['SUM(cantTo)']==None:
            sumTo[0]['SUM(cantTo)']=0    
        monedasDisponibles = sumTo[0]['SUM(cantTo)'] - sumFrom[0]['SUM(cantFrom)']
        self.spent= monedasDisponibles

        totalUSD =0.0
        diccionarioUSD = self.apiCalculate()


        for coinsToCalculate in Coins:
            coinFrom = {'coinFrom':coinsToCalculate[0]}
            print(coinFrom)
            consulta = "SELECT SUM(cantFrom) FROM compras WHERE coinFrom=:coinFrom"
            sumFrom = self.based.consultaSQL2(consulta,coinFrom)
            consulta = "SELECT SUM(cantTo) FROM compras WHERE coinTo=:coinFrom"
            sumTo = self.based.consultaSQL2(consulta,coinFrom)
            if sumFrom[0]['SUM(cantFrom)']==None:
                sumFrom[0]['SUM(cantFrom)']=0
            if sumTo[0]['SUM(cantTo)']==None:
                sumTo[0]['SUM(cantTo)']=0    
            monedasDisponibles = sumTo[0]['SUM(cantTo)'] - sumFrom[0]['SUM(cantFrom)']
            totalUSD+= monedasDisponibles*diccionarioUSD.setdefault(coinFrom['coinFrom'])

        self.currentValue = totalUSD/diccionarioUSD.setdefault('EUR')

    def apiCalculate(self):
        cabecera = {"X-CoinAPI-Key": APIKEY}
        respuesta = requests.get(URLTOTAL.format("EUR;BTC;ETH;XRP;LTC;BCH;BNB;USDT;EOS;BCHSV;XLM;ADA;TRX"), headers=cabecera)
        diccionarioUSD = {}
        if respuesta.status_code == 200:
            longitud = len(respuesta.json())
            for coin in respuesta.json():
                moneda = coin["asset_id"]
                price = coin["price_usd"]
                diccionarioUSD.setdefault(moneda,price)
            return diccionarioUSD
        else:
            raise APIError(f"Se ha producido el error {respuesta.status_code} en la peticion")
