#!/bin/bash
# Using https://github.com/rigtorp/c2clat
# Compiled on target with `clang++-12 -O3 -DNDEBUG c2clat.cpp -o c2clat -pthread`
# Run with `ssh ? 'sudo nice --10                      ~/git/c2clat/c2clat -s 10000'  >/tmp/out.txt && ~/el15066/c2clat.sh /tmp/out.txt`
# or       `ssh ? 'sudo nice --10 taskset -c 3-5,15-17 ~/git/c2clat/c2clat -s 100000' >/tmp/out.txt && ~/el15066/c2clat.sh /tmp/out.txt`

(
echo "set title 'Inter-core one-way data latency between CPU cores'"
echo "set xlabel 'CPU'"
echo "set ylabel 'CPU'"
echo "unset key"
echo "set cblabel 'Latency (ns)'"
#echo "plot fname matrix rowheaders columnheaders using 2:1:3 with image"
#echo "plot '$1' matrix rowheaders columnheaders using 2:1:3 with image"
echo "plot '$1' matrix rowheaders columnheaders using 2:1:3 with image,\\"
echo      "'$1' matrix rowheaders columnheaders using 2:1:(sprintf("'"%g", $3'")) with labels font ',6'"
) | tee /dev/stderr | gnuplot -p
#) | tee /dev/stderr | gnuplot -e "fname='$1'" -p
