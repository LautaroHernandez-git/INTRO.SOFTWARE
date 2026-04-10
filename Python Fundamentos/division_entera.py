num_a= int(input("Ingrese dividendo para ser dividido: "))
num_b= int(input("Ingrese divisor: "))

abs_a = abs(num_a)
abs_b = abs(num_b)

cociente=0 
resto= abs_a

while resto >= abs_b:
    resto= resto - abs_b
    cociente+=1

print(f"El cociente es: {cociente}")
print(f"El resto es: {resto}")

