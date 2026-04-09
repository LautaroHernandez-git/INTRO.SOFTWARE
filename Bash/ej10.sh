echo "escribe los tres lados de tu triangulo:"
read lado1
read lado2
read lado3

if [[ "$lado1" -eq "$lado2" && "$lado1" -eq "$lado3" ]]; then
    echo "Tu triangulo es equilatero"
elif [[ "$lado1" -eq "$lado2" || "$lado2" -eq "$lado3" || "$lado1" -eq "$lado3" ]]; then
    echo "Tu triangulo es isosceles"
else 
    echo "Tu triangulo es escaleno"
fi
