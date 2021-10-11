from . import app
from flask import render_template, request

@app.route("/")
def index():
    return render_template('pag_ini.html')

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
