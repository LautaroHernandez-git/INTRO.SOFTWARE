num= int(input("Un numero entero positivo entre el 1 y 3999"))

millares= num // 1000
centenas= (num % 1000) // 100
decenas= (num % 100) // 10
unidades= num % 10

if millares == 0:
    rom_m= " "
elif millares == 1:
    rom_m= "M"
elif millares == 2:
    rom_m= "MM"
elif millares == 3:
    rom_m= "MMM"
pass

if centenas == 0:
    rom_c= " "
elif centenas == 1:
    rom_c= "C"
elif centenas == 2:
    rom_c= "CC"
elif centenas == 3:
    rom_c= "CCC"
elif centenas == 4:
    rom_c= "CD"
elif centenas == 5:
    rom_c= "D"
elif centenas == 6:
    rom_c= "DC"
elif centenas == 7:
    rom_c= "DCC"
elif centenas == 8:
    rom_c= "DCCC"
elif centenas == 9:
    rom_c= "CM"
pass

if decenas == 0:
    rom_d= " "
elif decenas == 1:
    rom_d= "X"
elif decenas == 2:
    rom_d= "XX"
elif decenas == 3:
    rom_d= "XXX"
elif decenas == 4:
    rom_d= "XL"
elif decenas == 5:
    rom_d= "L"
elif decenas == 6:
    rom_d= "LX"
elif decenas == 7:
    rom_d= "LXX"
elif decenas == 8:
    rom_d= "LXXX"
elif decenas == 9:
    rom_d= "XC"
pass

if unidades == 0:
    rom_u= " "
elif unidades == 1:
    rom_u= "I"
elif unidades == 2:
    rom_u= "II"
elif unidades == 3:
    rom_u= "III"
elif unidades == 4:
    rom_u= "IV"
elif unidades == 5:
    rom_u= "V"
elif unidades == 6:
    rom_u= "VI"
elif unidades == 7:
    rom_u= "VII"
elif unidades == 8:
    rom_u= "VIII"
elif unidades == 9:
    rom_u= "IX"
pass

romano= rom_m + rom_c + rom_d + rom_u
input(f"Año pasado a romano: {romano} ")
