echo "Ingresa tu nombre"
read nombre 

if [ $nombre = "manu" ] || [ $nombre = "Manu" ]; then
     echo "Hola, profe!"
else
     echo "Hola $nombre"
fi


 