#!/usr/bin/env bash

for i in `seq 2 37`; do
    echo "Checking N =" $i
    ./prime-or-composite.py $i > examples/check_$i.log
done    


