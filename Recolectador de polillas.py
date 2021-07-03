# Se inicia una campaña de recolección de colillas de cigarrillos en los barrios.

# Realizá un programa que permita registrar cantidad de colillas recolectadas por un número
# determinado de personas. Luego obtener estadísticas al respecto informando porcentaje de personas
# que han encontrado menos de 100 colillas, más de 100 y menos de 200, más de 200 colillas.

colillas = int(input("Ingrese la cantidad de colillas que ha recolectado:   "))
persona = 1
per_mas100=0
per_menos100=0
per_mas200=0
total_colillas=0
while True:
    if colillas<100:
        per_menos100=per_menos100+1
    elif colillas>=100 and colillas<200:
        per_mas100=per_mas100+1
    elif colillas>=200:
        per_mas200=per_mas200+1
   
    total_colillas=total_colillas+colillas
    respuesta=input("Desea ingresar más información? Ingrese si o no?  ")
        

    if respuesta == "si":
        persona= persona+1
        colillas = int(input("Ingrese la cantidad de colillas que ha recolectado:   "))
    elif respuesta=="no":
        print("Ok. Veamos las estadisticas.")
        break
    else:
        print("Ingresa una opcion correcta")

print(f"""Cantidad de persona que participaron: {persona}
Pocentaje de personas que juntaron menos de 100 colillas: {per_menos100/persona*100} %
Pocentaje de personas que juntaron mas de 100 y menos de 200 colillas: {per_mas100/persona*100} %
Pocentaje de personas que juntaron mas de 200 colillas: {per_mas200/persona*100} %""")
