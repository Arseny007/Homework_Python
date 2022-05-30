#!/bin/bash

# C использованием функций сделать скрипт (bash), который копирует в папку (переданную как аргумент) все файлы, 
# в названии которых содержится шаблон (тоже переданный как аргумент)

while [ -n "$1" ]
do
    case "$1" in
    -d) papka="$PWD/$2/";;
    -f) example="$2";;
    esac
    shift
done

mkdir $papka

cpp () {
    cp $1 "$papka/"
}

list="$(ls -1 | grep $example)"
for value in $list
do
    cpp $value
done