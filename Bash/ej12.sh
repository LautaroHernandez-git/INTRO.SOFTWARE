echo "Dame un numero n:"
read numero

i=1
while [ $i -le $numero ]; do
    echo $i
    ((i+=1))
done

