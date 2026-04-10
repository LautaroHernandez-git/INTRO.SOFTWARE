n= int(input("Ingrese n para llegar a 1 en sucesion"))

maximo= n
paso= 0

while ( n > 1):
    if (n % 2 == 0):
      n= n // 2
      paso+=1
      if (n > maximo):
           maximo= n
    if (n % 2 != 0 and n != 1):
        n= 3 * n + 1
        paso+=1
        if (n > maximo):
          maximo= n
    

print(f"pasos: {paso}")
print(f"Maximo: {maximo}")

