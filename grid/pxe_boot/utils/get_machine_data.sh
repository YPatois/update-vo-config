#!/bin/bash

mkdir -p data

function get_one_machine_data() {
    echo "For machine: $wn"
    ssh -o ConnectTimeout=2 root@${wn} "ip a" > ./data/$wn.txt
}

export -f get_one_machine_data

WNlist=""
for wn in `grep sbgwn ../vault/ansible_data/hosts  | grep -v '#'`; do
    WNlist="$WNlist $wn"
done

parallel --line-buffer --jobs 64 get_one_machine_data ::: $WNlist
