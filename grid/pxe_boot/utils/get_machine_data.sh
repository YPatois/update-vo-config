#!/bin/bash

mkdir data

for wni in `seq 40 59`; do
    wn=sbgwn${wni}.in2p3.fr
    echo "Machine: $wn"
    ssh $wn "ip a" > ./data/$wn.txt
done
