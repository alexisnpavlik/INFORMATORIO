valor=float(input("Alimentame con valores: "))
i=1
subtotal=0
while i!=50:
    if valor==0:
        break
    elif i==49:
        print("Mejor usa Excel")
        break
    else:
        subtotal=subtotal+valor
    print(f"La cuenta es: {subtotal}")
    print("El promedio es "+str(subtotal/i))
    valor=float(input("Dame otro valor: "))
    i=i+1
print("Programa finalizado") 