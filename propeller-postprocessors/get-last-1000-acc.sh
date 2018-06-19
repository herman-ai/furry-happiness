for file in *.log; do grep -e "1$" $file | tail -n 1000 | grep "1 .$" | echo `(wc -l)` : $file ; done
