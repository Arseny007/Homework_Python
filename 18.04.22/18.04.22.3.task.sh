#!/bin/bash

exec 2>>errors_log

file=''
dir=''
while [ -n "$1" ]
do
    case "$1" in
    -f) 
    file="$2"
    shift;;

    -d)
    dir="$2"
    shift;;

    *) echo "ups";;
    esac
    shift
done


exec 2>errors_log
mkdir $dir
result=''

while IFS= read line
    do
    exec 1>norm_log
    exec 2>errors_log
    cp $line $dir && echo "$line moved to $dir"
    result=$line
    done < $file

trap "echo '$result'" EXIT