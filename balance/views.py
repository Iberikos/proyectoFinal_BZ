from datetime import datetime
from . import app
from flask import render_template, request, redirect, url_for, flash
from balance.models import DDBBmanager, CriptoValueModel, StatusModel
from balance.forms import MovFormulary
from balance import models


RUTA_DDBB = app.config.get("RUTA_DATABASE")
based = DDBBmanager(RUTA_DDBB)

@app.route("/")
def index():        
    consulta = "SELECT * FROM compras ORDER BY fecha"
    compras = based.consultaSQL(consulta)

    
    return render_template('pag_ini.html', items=compras)


@app.route("/purchase",  methods=['GET', 'POST'])
def buy():
    formulary = MovFormulary()
    now = datetime.now()
    formulary.date.data = now.strftime("%d-%m-%Y")
    formulary.time.data = now.strftime("%H:%M:%S")

    calculator_pushed = False
    if request.method == 'GET':
        formulary.cantTo.data=0
        return render_template("pag_purchase.html", formulario = formulary)
    else:
        
        if formulary.validate():

            if formulary.calcular.data:
                fcoin = request.values.get('coinFrom')
                tcoin = request.values.get('coinTo')
                cripto = CriptoValueModel(fcoin, tcoin)
                qf = request.values.get('cantFrom')
                if fcoin==tcoin:
                    flash("No se puede hacer un calculo con las mismas monedas")
                    return render_template("pag_purchase.html", formulario=formulary)                
                if fcoin != 'EUR':
                    print(formulary.data)
                    consulta = "SELECT SUM(cantFrom) FROM compras WHERE coinFrom=:coinFrom"
                    sumFrom = based.consultaSQL2(consulta,formulary.data)
                    consulta = "SELECT SUM(cantTo) FROM compras WHERE coinTo=:coinFrom"
                    sumTo = based.consultaSQL2(consulta,formulary.data)
                    if sumFrom[0]['SUM(cantFrom)']==None:
                        sumFrom[0]['SUM(cantFrom)']=0
                    if sumTo[0]['SUM(cantTo)']==None:
                        sumTo[0]['SUM(cantTo)']=0    
                    monedasDisponibles = sumTo[0]['SUM(cantTo)'] - sumFrom[0]['SUM(cantFrom)']
                    if  monedasDisponibles - float(qf) < 0:
                        flash("No dispones de monedas para comprar")
                        # print ( monedasDisponibles - float(qf))
                        return render_template("pag_purchase.html", formulario=formulary)                

                cripto.obtener()
                formulary.pu.data = cripto.valor
                formulary.cantTo.data = float(qf) * formulary.pu.data
                formulary.puH.data = formulary.pu.data
                formulary.cantToH.data = formulary.cantTo.data
                return render_template("pag_purchase.html", formulario=formulary)                
            else:
                try:
                    consulta = """
                    INSERT INTO compras (fecha, hora, coinFrom, cantFrom, coinTo, cantTo, pu)
                    VALUES (:date, :time, :coinFrom, :cantFrom, :coinTo, :cantToH, :puH)
                    """
                    print(formulary.data)
                    based.modificaSQL(consulta, formulary.data)
                except Exception as e:
                    # print("Hay un error en la base de datos", e)
                    flash("Hay un error en la base de datos")
                return redirect(url_for("index"))
        else:
            # flash("Debe ser un número entero y positivo")
            return render_template("pag_purchase.html", formulario = formulary)
    return render_template("pag_purchase.html", formulario = formulary)

@app.route("/status")
def status():
    #Consultar BBDD, copiar
    #Devolver pagina con datos

    status = StatusModel(based)
    status.calcular()
    status.apiCalculate()

    vectorDevolver = []
    vectorDevolver.append(status.spent)
    vectorDevolver.append(status.currentValue)
    return render_template("pag_status.html",items=vectorDevolver)
