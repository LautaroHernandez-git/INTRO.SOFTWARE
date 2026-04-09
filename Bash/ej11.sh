echo "Escribe dos numeros y la operacion que dea realizar"
read numero1
read numero2
read op

if [ "$op" = "multiplicacion" ] || [ "$op" = "Multiplicacion" ]; then
    mult=$(( numero1 * numero2 ))
    echo "Tu operacion da: $mult"
elif [ "$op" = "division" ] || [ "$op" = "Division" ]; then
    div=$(( numero1 / numero2 ))
    echo "Tu operacion da: $div"
elif [ "$op" = "suma" ] || [ "$op" = "Suma" ]; then
    sum=$(( numero1 + numero2 ))
    echo "Tu operacion da: $sum"
elif [ "$op" = "resta" ] || [ "$op" = "Resta" ]; then
    res=$(( numero1 - numero2 )) 
    echo "Tu operacion da: $res"
else
    echo "error"
fi

