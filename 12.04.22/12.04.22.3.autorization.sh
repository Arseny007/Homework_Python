#!/bin/bash

echo "LOG IN"
flag=$true
file="namefile.txt"
while $flag
do
    read -p "Enter your name" name
    cat $file | while read line
    do 
        if [[ "$name" == "$line"* ]]
        then
        echo "Name exist"
        for i in [ 1, 2, 3 ]
        do
            read -s -p "try: $i Enter your password" password
            echo $password | sha256sum > temp.txt
            cat $file | while read line
            do 
                if [[ "cat temp.txt" == *"$line"* ]]
                then
                echo "log in success"
                break
                flag=$false
                fi
            done
            if $flag==$false
            then
            break
            fi
        done
        else
        echo "name not exist. try again"
        break
        fi
    done
done