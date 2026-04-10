def campesina_rusa(a,b):
    resultado= 0 
    while b > 0:
        if b & 1 == 1:
            resultado += a
        a= a << 1
        b= b >> 1
    return resultado

def multiplicar(a,b):
    signo= 1
    if a < 0 or b < 0:
       signo= -1
    if a < 0 and b < 0:
       signo= 1
    abs_a= abs(a)
    abs_b= abs(b)
    resultado= campesina_rusa(abs_a, abs_b) * signo
    return resultado 

num_a= int(input("Ingrese num A para ser multiplicado"))

num_b= int(input("Ingrese num B para ser multiplicado"))

print(f"tu resultado es {multiplicar(num_a, num_b)}")

