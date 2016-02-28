#!/bin/bash
function bajar () {
  cd $1
  echo descargando : $1
  wget -c -i links.txt
  cd ..
  echo completo
  prog=$1
  sed '1d' pendientes.txt > temp.txt
  rm pendientes.txt
  mv temp.txt pendientes.txt 
  echo $1 >> completos.txt
}
while read line
do
  programa="$line"
  echo "bajando paquetes para:"
  echo $programa
  bajar $programa
done < pendientes.txt