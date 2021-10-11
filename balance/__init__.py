from flask import Flask

app = Flask(__name__)

from . import views


APIKEY = "05915253-A982-431B-87AA-55C645B31B41"
URL = "https://rest.coinapi.io/v1/exchangerate/BTC/EUR"

MONEDAS = ["EUR - Euro", 
            "USD - Dolar",
            "BTC - Bitcoin",
            "ETH - Ethereum",
            "BNB - Binance coin",
            "ADA - Cardano"]