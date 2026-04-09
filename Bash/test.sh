echo "cuantos DNI vas a ingresar"
read num
dnis=()

for (( i=1; i<=num; i++ )) ; 
do
   echo "Ingrese DNI"
   read dni
   dnis+=("$dni")
done

printf "Dnis ordenados por edad mayor a menor\n"
printf "%s\n" "${dnis[@]}" | sort -n




