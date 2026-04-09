echo "Nombra tu primer archivo:"
read nom1
echo "Que va a contener:"
read con1
echo $con1 > "$nom1.txt"
 
echo "Nombra tu segundo archivo:"
read nom2
echo "Que va a contener:"
read con2
echo $con2 > "$nom2.txt"

echo -e "$con1\n$con2" > "concatenados.txt"

