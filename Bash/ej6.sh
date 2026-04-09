echo "Dame un numero"
read numero 

if [ $numero -eq 0 ]; then
    echo "Tu numero es igual a 0"
elif [ "$numero" -gt 0 ]; then 
    echo "Tu numero es mayor que 0"
elif [ "$numero" -lt 0 ]; then
    echo "Tu numero es menor que 0"
else
    echo "error"
fi
