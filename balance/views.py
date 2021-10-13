from . import app
from flask import render_template, request
import sqlite3


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

@app.route("/apiCoin", methods=['POST'])
def prueba():
    print(request.form)
    return render_template("pag_purchase.html")
#Funcion con route /apiCoin
#Consultar con dos valores del html a apicoin
#Actualizar variable global var conversor
#Si hay datos 

#Cada vez que se actualize los numeros del from de la pagina
#Llamar a otra url que multiplica 

#Crear funcion con app,route '/introducir'
#Insertar en BBDDD
#Redirect a Status
