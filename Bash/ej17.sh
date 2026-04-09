echo "Ingresa cuantos dnis vas a usar"
read n

Dnis=()

for (( i=1; i<=n; i++ ))
do
   echo "Ingrese DNI " $i
   read dni
   dnis+=("$dni")
done

ordenados=$( printf "%s\n" "${dnis[@]}" | sort -n )


echo -e "DNIS INGRESADOS\n" $ordenados

