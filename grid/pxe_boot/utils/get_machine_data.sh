#!/bin/bash

mkdir data

for wn in `grep sbgwn ../vault/ansible_data/hosts  | grep -v '#'`; do
    echo "Machine: $wn"
    ssh -o ConnectTimeout=2 $wn "ip a" > ./data/$wn.txt
done
