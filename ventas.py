import pandas as pd

nombre_planilla=input("ingrese el nombre de la plantilla ")

ventas=pd.read_excel(nombre_planilla,sheet_name="Ventas")

#print(ventas)
#print(ventas.describe())

#print(ventas["Precio_Unitario"])

ventas["Facturacion"]=ventas["Precio_Unitario"]*ventas["Unidades"]
(print(ventas["Facturacion"]))