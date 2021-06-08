import random

number_random=random.randint(1,100)
number_select=int(input("""Adivina el numero del 1 al 100, Tienes 10 intentos
Mi numero elegido es el: """))
i=1
while i<10:
    if number_select < number_random:
        number_select=int((input("Incorrecto, el numero es mas grande ¡VUELVE A INTENTAR!: ")))
    elif number_select > number_random:
        number_select=int(input("Incorrecto, el numero es mas pequeño ¡VUELVE A INTENTAR!: "))
    elif number_select==number_random:
        print(f"¡ADIVINASTE! el numero era el {number_select}")
        break
    i=i+1
if i <10:
    print(f"Te tomo {i} intentos")
else:
    print("Mala suerte, la proxima usa el algorito de la tangente entre dos puntos")

    

gfgfg