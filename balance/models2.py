import csv

ruta_basedatos = "data/compras.csv"

class Compras():
    def __init__(self, fecha, hora, coinFrom, cantFrom, coinTo, cantTo, Pu):
        self.fecha = fecha
        self.hora = hora
        self.coinFrom = coinFrom
        self.cantFrom = cantFrom
        self.coinTo = coinTo
        self.cantTo = cantTo
        self.Pu = Pu

class ListaCompras():
    def __init__(self):
        self.compras = []

    def leer(self):
        basedatos = open(ruta_basedatos, "r")
        dreader = csv.DictReader(basedatos)
        for linea in dreader:
            self.compras.append(linea)

        basedatos.close()
    
    def escribir(self):
        basedatos = open(ruta_basedatos, "w")
        nombres_campo = list(self.compras[0].keys())
        dwriter = csv.DictWriter(basedatos, fieldnames=nombres_campo)
        for compra in self.compras:
            dwriter.writerow(compra)
        basedatos.close()