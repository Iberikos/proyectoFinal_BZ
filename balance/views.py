import flask
from . import app
from flask import render_template, request
import sqlite3
from balance import models


@app.route("/")
def index():
    conn = sqlite3.connect("data/Compras.db")

    cur = conn.cursor()
    cur.execute("SELECT * FROM compras order by fecha;")
    
    keys = []
    for item in cur.description:
        keys.append(item[0])

    compras = []
    for registro in cur.fetchall():
        ix_clave = 0
        d = {}
        for columna in keys:
            d[columna] = registro[ix_clave]
            ix_clave += 1
        compras.append(d)
    
    return render_template('pag_ini.html', items=compras)


@app.route("/purchase")
def buy():
    return render_template("pag_purchase.html")

@app.route("/status")
def status():
    #Consultar BBDD, copiar
    #Devolver pagina con datos

    return render_template("pag_status.html")

@app.route("/apiCoin")
def prueba():
    listaValores = flask.request.values
    coinFrom = listaValores.get('from')
    coinTo = listaValores.get('to')

    conversor = models.ConversorMoneda()
    print(flask.request.values)
    
    cripto = models.CriptoValueModel(conversor.convertirStringMoneda(coinFrom),conversor.convertirStringMoneda(coinTo))
    cripto.obtener()
    print(cripto.valor)
    return render_template("pag_purchase.html")
#Funcion con route /apiCoin
#Consultar con dos valores del html a apicoin
#Actualizar variable global var conversor si hay datos

#Cada vez que se actualize los numeros del from de la pagina
#Llamar a otra url que multiplica 

#Crear funcion con app,route '/introducir'
#Insertar en BBDDD
#Redirect a Status
#crear en un nuevo archivo PY un objeto que mueva la BBDD

#No dejar hacer compras sin haber rellenado los datos de compras