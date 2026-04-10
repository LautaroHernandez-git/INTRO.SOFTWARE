a = float(input("Ingrese el término 'a' de la ecuación cuadrática: "))
b = float(input("Ingrese el término 'b' de la ecuación cuadrática: "))
c = float(input("Ingrese el término 'c' de la ecuación cuadrática: "))

discriminante = b ** 2 - 4 * a * c
x1 = (-b + discriminante ** 0.5) / (2 * a)
x2 = (-b - discriminante ** 0.5) / (2 * a)

print(round(discriminante))
print(f"{x1:.4f}")
print(f"{x2:.4f}")