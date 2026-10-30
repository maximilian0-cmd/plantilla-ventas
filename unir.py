import pandas as pd
import matplotlib.pyplot as plt

primer_mes = input("Primer mes de comparación (archivo): ")
segundo_mes = input("Segundo mes de comparación (archivo): ")

# CTRL K CTRL C
#print(primer_mes)
#print(segundo_mes)

# CTRL K CTRL C
ventas_mes_1 = pd.read_excel(primer_mes, sheet_name="Ventas")
ventas_mes_2=pd.read_excel(segundo_mes,sheet_name="Ventas")

#print(ventas_mes_1)
#print(ventas_mes_2)

print(f"Filas {primer_mes}: {len(ventas_mes_1)} | Filas {segundo_mes}: {len(ventas_mes_2)}")

ventas=pd.concat([ventas_mes_1,ventas_mes_2],ignore_index=True)

#print(ventas)
#print(len(ventas))

print(f"Cantidad de Filas de la union: {len(ventas)}")

ventas["Facturacion"]=ventas["Precio_Unitario"]*ventas["Unidades"]

negocios=pd.read_excel(primer_mes, sheet_name="Negocios")


ventas=ventas.merge(negocios,on="Negocio",how="left")


#print(ventas)

totales=ventas.groupby("Mes", sort=False)[["Unidades", "Facturacion"]].sum()

print(totales)

fig, ejes = plt.subplots(1, 2, figsize=(13, 6))
fig.suptitle("Comparación de ventas de alfajores", fontsize=16, fontweight="bold")

totales["Unidades"].plot(kind="bar",ax=ejes[0],rot=0,title="Unidades Vendidas",color=["blue", "skyblue"])
totales["Facturacion"].plot(kind="bar",ax=ejes[1],rot=0,title="Total Facturado",color=["steelblue", "orange"])

ejes[0].bar_label(ejes[0].containers[0])
ejes[1].bar_label(ejes[1].containers[0])

plt.show()
