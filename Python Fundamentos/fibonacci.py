num_entero_positivo = int(input("Ingrese un número entero no negativo: "))
num_oro = (1 + 5 ** 0.5) / 2
conjugado_num_oro = (1 - 5 ** 0.5) / 2

fx_oro = (num_oro ** num_entero_positivo) / 5 ** 0.5
binet = round((num_oro ** num_entero_positivo - conjugado_num_oro ** num_entero_positivo) / 5 ** 0.5)


print(binet)
print(fx_oro)
print(round(fx_oro))