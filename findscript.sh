#!/bin/bash
mkdir $1

for file in $(ls $PWD/alldir)
do
dirr=$(cat alldir/$file)
case $dirr in
  *"$1"*) cp alldir/$file $1/$file ;;
esac
done