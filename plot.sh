#!/bin/bash

python3 wave.py -f 1 > series.txt

echo -n "mean: "
python3 mean.py series.txt

# python3 wave.py -f 6 > series2.txt
# python3 wave.py -f 2 -p 5 -v -3 > series3.txt
# python3 combine.py series.txt series2.txt series3.txt > series4.txt
python3 plot.py series.txt -o ~/site/web/downloads/plot 
