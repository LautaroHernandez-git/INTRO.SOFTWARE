echo "Dame un numero para calcular su factorial"
read numero

factorial=1

for ((i=1; i<=$numero; i++));
do 
    (( factorial *= $i ))
done 

echo "Este es el resultado;" $factorial

    