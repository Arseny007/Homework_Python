#!/bin/bash

trap "echo 'Nothing can stop me now'" SIGINT
# trap "echo 'goodbye...;((('" EXIT

count=1
while [[ $count -le 5 ]]
do
    echo "msg #$count"
    count=$(($count+1))
    sleep 3
done


trap -- SIGINT
while [[ $count -le 10 ]]
do
    echo "msg #$count"
    count=$(($count+1))
    sleep 3
done
