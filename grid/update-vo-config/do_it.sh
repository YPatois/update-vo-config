#!/bin/bash

token=$1

./update-vo-config -b mytest  -t $token --use-pickle

rm -rf mytest/vocopy
mkdir -p mytest/vocopy/params
cp mytest/vo/params/a* mytest/vocopy/params/
#cp mytest/vo/params/c* mytest/vocopy/params/
