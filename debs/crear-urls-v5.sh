#!/bin/bash
echo "Creando lista de descargas para :"
for ((i=1;i<=$#;i++)) 
do
  eval "echo \${$i}"
  eval "mkdir \${$i}"
  eval "cd \${$i}"
  eval "sudo apt-get -qq --print-uris install \${$i} linux-headers-$(uname -r) | cut -d\' -f 2 >links.txt"
  cd ..
  eval "programa=\${$i}"
  echo $programa  >> pendientes.txt
  echo $programa  >> pendientes-aux.txt
done
echo "..."
cd ..
echo "echo :)"
