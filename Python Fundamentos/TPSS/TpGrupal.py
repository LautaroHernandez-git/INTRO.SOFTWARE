# ============================
# SECCION DECLARATIVA
# ============================











# ==========================================
# SECCIÓN DE DEFINICIÓN DE FUNCIONES
# =========================================


def busqueda_interpolacion(datos,clave, contar = False):
    '''
    SECCIÓN DECLARATIVA
    Descripción: Buscar la posición de 'clave' en la secuencia ordenada 'datos'
        usando búsqueda binaria (versión iterativa).
    Precondición: datos está ordenado de menor a mayor.
    Postcondición: retorna el índice i tal que datos[i] == clave,
        o -1 si clave no pertenece a datos.
    '''

    # --- SECCIÓN ALGORÍTMICA ---
    
    # Prólogo: definir la región de búsqueda
    if contar == True: #Activador de contador 
        contador= 0 
    izq = 0
    der = len(datos) - 1

    while izq <= der and datos[izq] <= clave <= datos[der]:
        contador+=1 #Suma al contador de comparaciones cada vez que se interacciona hasta que encuentre la clave
        # Evitar división por cero cuando todos los valores son iguales
        if datos[izq] == datos[der]:
            if datos[izq] == clave:
                return izq, contador
            else:
                return -1, contador
        
        # Estimar posición por interpolación lineal
        pos = izq + (clave - datos[izq]) * (der - izq) // (datos[der] - datos[izq])


        if datos[pos] == clave:
            return pos, contador
        elif datos[pos] < clave:
            izq = pos + 1
        else:
            der = pos - 1

    return -1, contador

def busqueda_binaria(datos, clave,contar = False):
    '''
    SECCIÓN DECLARATIVA
    Descripción: Buscar la posición de 'clave' en la secuencia ordenada 'datos'
        usando búsqueda binaria (versión iterativa).
    Precondición: datos está ordenado de menor a mayor.
    Postcondición: retorna el índice i tal que datos[i] == clave,
        o -1 si clave no pertenece a datos.
    '''

    # --- SECCIÓN ALGORÍTMICA --

    # Prólogo: definir la región de búsqueda
    if contar == True: #Activador de contador
        contador= 0 
    izq = 0
    der = len(datos) - 1

    # Resolución: dividir la región a la mitad en cada paso
    while izq <= der:
        contador+=1 #Suma al contador de comparaciones cada vez que se interacciona hasta que encuentre la clave
        medio = (izq + der) // 2

        if datos[medio] == clave:
            return medio , contador             # encontrado
        elif clave < datos[medio]:
            der = medio - 1        # descartar mitad derecha
        else:
            izq = medio + 1        # descartar mitad izquierda

    # Epílogo: la región quedó vacía (izq > der)
    return -1 , contador                  # no encontrado

# ==========================================
# SECCIÓN PRINCIPAL
# =========================================

#1) Prologo:
import random
import numpy as np
print("--Búsqueda por interpolación vs. búsqueda binaria--")


#2)Desarrollo Escenario A:
n= 10000
datosA= sorted(random.sample(range(1,100001), n))
clavesA= random.sample(datosA, 500)
ind_interA= []
ind_binA= []
cont_interA= []
cont_binA= []

for clave in clavesA:
    resultado_interpolacionA= busqueda_interpolacion(datosA,clave,contar= True)
    if resultado_interpolacionA[0] != -1:
        ind_interA.append(resultado_interpolacionA[0])
        cont_interA.append(resultado_interpolacionA[1])
    else:
        ind_interA.append("No lo encontre")
        cont_interA.append(resultado_interpolacionA[1])
    resultado_binarioA= busqueda_binaria(datosA, clave,contar = True)
    if resultado_binarioA[0] != -1:
        ind_binA.append(resultado_binarioA[0])
        cont_binA.append(resultado_binarioA[1])
    else: 
        ind_binA.append("No lo encontre")
        cont_binA.append(resultado_binarioA[1])

#3)Desarrollo Escenario B:
vals = set()
while len(vals) < n:
  vals.add(int(random.expovariate(1) * 10000))
datosB= sorted(vals)
clavesB= random.sample(datosB, 500)
ind_interB= []
ind_binB = []
cont_interB= []
cont_binB= []

for clave in clavesB:
    resultado_interpolacionB= busqueda_interpolacion(datosA,clave,contar= True)
    if resultado_interpolacionB[0] != -1:
        ind_interB.append(resultado_interpolacionB[0])
        cont_interB.append(resultado_interpolacionB[1])
    else:
        ind_interB.append("No lo encontre")
        cont_interB.append(resultado_interpolacionB[1])
    resultado_binarioB= busqueda_binaria(datosB, clave,contar = True)
    if resultado_binarioB[0] != -1:
        ind_binB.append(resultado_binarioB[0])
        cont_binB.append(resultado_binarioB[1])
    else: 
        ind_binB.append("No lo encontre")
        cont_binB.append(resultado_binarioB[1])

print(np.mean(ind_interB))
print(np.mean(ind_binB))
print(np.mean(cont_interB))
print(np.mean(cont_binB))




    
        


    




