var=int(input("""cual es el Tamaño del pez, Ingrese la opcion correcta
    1- Normal
    2- Denajo de Normal
    3- Por arriba de lo Normal
    4- Sobre Dimencionado
    """))
nor=0
denor=0
arr_nor=0
sobre=0
while var!=0:
    if var==1:
        print("Pez en buenas condiciones")
        nor=nor+1
    elif var==2:
        print("Pez con problemas de nutrición")
        denor=denor+1
    elif var==3:
        print("Pez con síntomas de organismo contaminado")
        arr_nor=arr_nor+1
    elif var==4:
        print("Pez contaminado")
        sobre=sobre+1
    else:
        print("Ingrese un opcion correcta")
    var=int(input("""
    cual es el Tamaño del pez, Ingrese la opcion correcta
    1- Normal
    2- Denajo de Normal
    3- Por arriba de lo Normal
    4- Sobre Dimencionado
    """))

print(f"Hay Normales {nor}")
print(f"Hay Denajo de Normal {denor}")
print(f"Por arriba de lo Normal {arr_nor}")
print(f"Sobre Dimencionados {sobre}")