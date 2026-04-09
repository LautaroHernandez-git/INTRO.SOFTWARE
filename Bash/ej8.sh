echo "dame un numero"
read numero 

if [ $(( numero % 2 )) -eq 0 ]; then
     echo "Es par!"
elif [ $(( numero % 2 )) -ne 0 ]; then
     echo "Es impar!"
else
     echo "error"
fi
