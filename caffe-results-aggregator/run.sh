#!/bin/bash

set -e

for fname in *.txt
    do
        echo "Working on ${fname}"
        cat ${fname} \
            | grep "Test net output #0\|Testing net" \
            | sed 's/Iteration//;s/, Testing net (#0)//;s/Test net output #0: accuracy = //;s/.*]//' \
            > ${fname}.csv

        paste - - < ${fname}.csv \
            | sponge ${fname}.csv

    done

for fname in *.csv
do
    sed -i.bak 1i"  Iteration    ${fname}" ${fname}
done



paste *.csv | column -s $'\t' -t > result.csv


