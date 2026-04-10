num_a= int(input("Ingrese num A para ser multiplicado"))

num_b= int(input("Ingrese num B para ser multiplicado"))
           
if (num_a or num_b < 0):
   signo= -1
else: 
   signo= 1


abs_a = abs(num_a)
abs_b = abs(num_b)

mayor = max(abs_a,abs_b)
menor = min(abs_a,abs_b)

producto= 0

for veces in range(menor):
   producto= producto + mayor

producto_final= producto * signo

print(f"Este es tu prodcuto {producto_final}")



