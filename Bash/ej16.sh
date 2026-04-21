numeros=()

while true; do
   echo "Ingrese numero... (si no desea ingresar mas numeros escribe NONE)"
   read i

   numeros+=("$i")

   if [ "$i" == "NONE" ]; then
      echo "Se da por terminada la ejecución"
      break
   fi

done
 
unset numeros[${#numeros[@]}-1]
printf "Su lista ingresada es: "
printf "%s," "${numeros[@]}"


