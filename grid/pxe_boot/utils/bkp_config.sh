#!/bin/bash
# Backup some config files to help debuging ansible issues

DATED=`date +"%s"`

BKP_DIR=/opt/tmp/conf_bkp/$DATED

MACHINE_LIST="sbgce1.in2p3.fr sbgwn49.in2p3.fr sbgwn50.in2p3.fr"

DIRS="/etc /root /home/ypatois /home/cms001 /home/griduser"

# FIXME: Something about rights puzzled me
mkdir -p $BKP_DIR 
for machine in $MACHINE_LIST; do
    mkdir -p $BKP_DIR/$machine
    for dir in $DIRS; do
        rsync -av $machine:$dir $BKP_DIR/$machine
    done
done

