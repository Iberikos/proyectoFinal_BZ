from . import app
from flask import render_template, request
from balance.models import DDBBmanager
from balance.forms import MovFormulary
from balance import models


RUTA_DDBB = app.config.get("RUTA_DATABASE")
based = DDBBmanager(RUTA_DDBB)

@app.route("/")
def index():        
    
    compras = based.consultaSQL("SELECT * FROM compras ORDER BY fecha")

    
    return render_template('pag_ini.html', items=compras)


@app.route("/purchase",  methods=['GET', 'POST'])
def buy():
    formulary = MovFormulary()







    return render_template("pag_purchase.html", formulario = formulary)

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