fecha= int(input("Seleccione su fecha a traves de AAAAMMDD"))

anio= int(fecha//100)
mes= int(fecha//100) % 100
dia= int(fecha % 100)

if mes == 1 or mes == 2: 
    mes += 12
    anio -= 1
pass

k= int(anio % 100)
j= int(anio //100)

h= (dia + (13*(mes+1)//5)+k+(k//4)+(j//4)-(5*j)) % 7

if h == 0:
    print("Sábado")
elif h == 1:
    print("Domingo")
elif h == 2: 
    print("Lunes")
elif h == 3: 
    print("Martes")
elif h == 4: 
    print("Miercoles")
elif h == 5: 
    print("Jueves")
elif h == 6: 
    print("Viernes")
else:
    print("ERROR")

    


 