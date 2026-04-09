echo "Dame un numero para ver cuantas carpetas creo"
read num

for (( i=1; i<=num; i++))
do
   mkdir "Carpeta$i"
done