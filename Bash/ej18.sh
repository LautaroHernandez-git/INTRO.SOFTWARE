echo "Introduce la contraseña"
read con 

while [ $con != "Viku1502" ]
do
   echo "Incorrecto vuelve a intentarlo"
   read con
done

echo "Contraseña correcta"

