#!/bin/bash

echo "LOG UP"
while true
do  
    find=$false
    read -p "Enter your login: " name
    file="namefile.txt"
    cat $file | while read line
    do
        if [[ "$name" == *"$line"* ]]
        then
        echo "This name already exist"
        find=$true
        break
        fi
    done
    if [ "$find" == "$false" ]
    then
    break
    fi
done
echo $name >> namefile.txt
read -s -p "Enter your password: " password
echo "$password" | sha256sum >> $file