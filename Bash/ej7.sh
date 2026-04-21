echo "Ingrese su edad para verificar si usted es mayor o menor"
read edad 

if [ "$edad" -ge 18 ]; then
    echo "Usted es mayor de edad"
else 
    echo "Usted es menor de edad"
fi

