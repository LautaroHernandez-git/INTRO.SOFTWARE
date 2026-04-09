echo "escribe un numero natural y que no sea 0"
read nat

for (( i=1; i<=nat; i++ ))
do 
   echo $USER > "archivo$i.txt"
done 

