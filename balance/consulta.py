from flask import requests

@app.route("/prueba")
def nuevo():
    url = 'https://rest.coinapi.io/v1/exchangerate/BTC/EUR'
    apikey = "05915253-A982-431B-87AA-55C645B31B41"

    head = {"x-CoinAPI-Key": apikey}
    respuesta = requests.get(url, headers=head)

    if respuesta.status_code == 200:
        print(respuesta.text)

