#!/bin/bash

trap "echo 'Trapped Ctrl-C'" SIGINT

count=1
while [[ $count -le 10 ]]
do
    echo "msg #$count"
    count=$(($count+1))
    sleep 1
done