comedor_det=[35,35,40,35,0,0,20] #35
comedor_lav=[15,15,15,15,5,5,0] #15
comedor_ese=[20,20,20,20,15,10,20] #20


mantenimiento_ese=[60,60,60,60,0,50,25] #60
mantenimiento_lav=[80,80,80,80,0,0,0] #80


def promedio(t):
    cont_det=0
    for i in t:
        cont_det=cont_det+i
    promedio_f=cont_det/len(t)
    promedio_f=round(promedio_f,2)
    return promedio_f

def run():
    print(f"""El estimado del comedor es: 
    Detegente: {promedio(comedor_det)} litros
    Lavandina: {promedio(comedor_lav)} litros
    Esencia: {promedio(comedor_ese)} litros"""
    )

    print(f"""El estimado de Mantenimiento es: 
    Lavandina: {promedio(mantenimiento_lav)} litros
    Esencia: {promedio(mantenimiento_ese)} litros""")

if __name__=='__main__':
    run()
