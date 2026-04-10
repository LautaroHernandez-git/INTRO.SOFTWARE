def digito_a_romano(digito, uno, cinco, diez):
    if digito == 0:
        return ""
    elif digito <= 3:
        return uno * digito
    elif digito == 4:
        return uno + cinco
    elif digito <= 8:
        return cinco + uno * (digito - 5)
    elif digito == 9:
        return uno + diez
     
def decimal_a_romano(numero):
    millares= numero // 1000
    centenas= (numero % 1000) // 100
    decenas= (numero % 100) // 10
    unidades= numero % 10

    romano= " "
    romano+= "M" * millares
    romano+= digito_a_romano(centenas, "C", "D", "M")
    romano += digito_a_romano(decenas, "X", "L", "C")
    romano += digito_a_romano(unidades, "I", "V", "X")

    return romano

def validar_rango(numero, minimo, maximo):
    return minimo <= numero <= maximo


numero = int(input("Ingrese un número entre 1 y 3999: "))

if validar_rango(numero, 1, 3999):
    print(decimal_a_romano(numero))
else:
    print("Número fuera de rango")

