#!/usr/bin/env bash

echo "Bash version ${BASH_VERSION} ..."

for i in {2..37} 1783
do
    echo "running N =" $i
    ./prime-or-composite.py $i > examples/check_$i.log
done



