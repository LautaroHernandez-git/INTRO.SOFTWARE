inicializar() { 
     mkdir -p entregas
     mkdir -p entregas/originales
     mkdir -p entregas/procesadas
     mkdir -p entregas/burlas





}

crear_archivos() {
    echo "cuantos archivos de alumnos vas a crear?"
    read cant

    for (( i=1; i<=cant; i++ ))
    do 
       echo "Ingrese nombre del alumno"
       read nom
       echo "Ingrese apellido del alumno"
       read ape
       echo "Ingrese padron del alumno"
       read pad

       echo "Alumno: $nom, $ape - Padron: $pad" > "entregas/originales/entrega_${nom}_${ape}.txt"

    done 

}

procesar() {

    for archivo in entregas/originales/*;
    do 
       if grep -Eq "^Alumno: [A-Za-z]+( [A-Za-z]+)*, [A-Za-z]+ - Padron: [0-9]{6}?" "$archivo"; then
            padron=$(grep -oE "[0-9]{6}?" "$archivo")
            cp "$archivo" "entregas/procesadas/${padron}.txt"
            echo "Verificacion lograda con exito"
            
        else
            echo "Error"
        fi  


    done

    for archivo in entregas/procesadas/*;
    do
        sed -i " " "1d" "$archivo"
    done

    for archivo in entregas/procesadas/*;
    do 
       primera_linea=$(head -n 1 "$archivo")
       if [[ -n "$primera_linea" ]]; then
          rm "$archivo"
       fi
    done
    






}

burlarme () {

    for archivo in entregas/procesadas/*;
    do
       cp "$archivo" "entregas/burlas"
    done 

    for archivo in entregas/burlas/*;
    do
       sed -i ' ' 's/[aeiouAEIOU]/i/g' "$archivo"
    done











x

}


case $1 in 
   inicializar)
      inicializar
      ;;
    crear_archivos)
      crear_archivos
       ;;
    procesar)
      procesar
      ;;
    burlarme)
      burlarme
      ;;
esac






