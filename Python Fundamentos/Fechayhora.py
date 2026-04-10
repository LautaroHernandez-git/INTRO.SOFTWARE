dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

hora = int(input("Ingrese la hora: "))
minutos = int(input("Ingrese los minutos: "))

parte_entera = año * 10000 + mes * 100 + dia

fraccion_dia = hora / 24 + minutos / (24 * 60)

fecha_hora = parte_entera + fraccion_dia

print(parte_entera)
print(f"{round((fraccion_dia * 100), 2)}% del dia")
print(fecha_hora)