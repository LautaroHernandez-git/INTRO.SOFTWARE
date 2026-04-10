fecha1= int(input("Seleccione su fecha a traves de AAAAMMDD"))
fecha2= int(input("Seleccione su fecha a traves de AAAAMMDD"))

def enfoqueA (fecha1,fecha2):
    anio1= int(fecha1//10000)
    mes1= int(fecha1//100) % 100
    dia1= int(fecha1 % 100)

    anio2= int(fecha2//10000)
    mes2= int(fecha2//100) % 100
    dia2= int(fecha2 % 100)

    if anio1 > anio2:
        dif_anio = (anio1 - anio2)
    elif anio1 < anio2:
        dif_anio = (anio2 - anio1)
    else:
        dif_anio = 0
    
    if mes1 > mes2:
        dif_mes = (mes1 - mes2)
    elif mes1 < mes2:
        dif_mes = (mes2 - mes1)
    else:
        dif_mes = 0
    
    if dia1 > dia2:
        dif_dia = (dia1 - dia2)
    elif dia1 < dia2:
        dif_dia = (dia2 - dia1)
    else:
        dif_dia = 0
    
    print(f"La diferencia es de: {dif_anio} años, {dif_mes} meses y {dif_dia} dias")
 

def enfoqueB(fecha1, fecha2):
    
    dif= abs(fecha1 - fecha2)
    anio= int(dif//10000)
    mes= int(dif//100) % 100
    dia= int(dif % 100)

    print(f"La diferencia es de: {anio} años, {mes} meses y {dia} dias")

enf= input("Elige el enfoque")

if enf == "A":
    enfoqueA(fecha1,fecha2)
elif enf == "B":
    enfoqueB(fecha1,fecha2)
else:
    print("ERROR")






    





    





