#!/bin/bash
# Backup some config files to help debuging ansible issues

BKP_DIR=/opt/tmp/conf_bkp

MACHINE_LIST="sbgce1.in2p3.fr sbgwn49.in2p3.fr sbgwn50.in2p3.fr"

DIRS="/etc /root /home/ypatois /home/vosbgin2p3fr001"

# FIXME: Something about rights puzzled me
mkdir -p $BKP_DIR 
for machine in $MACHINE_LIST; do
    mkdir -p $BKP_DIR/$machine
    for dir in $DIRS; do
        rsync -av $machine:$dir $BKP_DIR/$machine
    done
done

