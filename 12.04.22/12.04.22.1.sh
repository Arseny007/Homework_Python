#!/bin/bash

# total=$[ $1 + $2 ]
# echo "args: $1 $2 $3 $4 $4 $5 $6 $7 $8 $9 ${10}"

# if [ -n "$1" ]
# then 
# echo "The number of given agrs: $#"
# # echo "Hello, $1"
# else
# echo "No arg given"
# fi

# echo "All args: $*"
# echo "All agrs[2]: $@"

####################################################

# count=1
# for arg in "$*"
# do
# echo "Arg number $count is $arg"
# count=$(( $count + 1 ))
# done

# count=1
# for arg in "$@"
# do
# echo "Arg number $count is $arg"
# count=$(( $count + 1 ))
# done

####################################################

# count=1
# while [ -n "$1" ]
# do
# echo "Arg number $count is $1"
# count=$(( $count + 1 ))
# shift
# done

######################################################

# while [ -n "$1" ]
# do
#     case "$1" in
#     -d) directory="$2"
#     echo "Dir $directory found"
#     shift;;
#     -b) parampampam="$2"
#     echo "Arg -b found with parametr $parampampam"
#     shift;;
#     --) shift
#     break;;
#     *) echo "$1 not supported";;
#     esac
#     shift
# done
# count=1
# for arg in "$@"
# do
# echo "@: Arg number $count is $arg"
# count=$(( $count + 1 ))
# done

###################################################

# echo "Enter your name: "
# read -p "Enter your name: " name s_name
# echo "Hell, $name $s_name"

###

# read -p "Enter your name: "
# echo "hell, $REPLY"
# read -s -p "Enter your password: "
# echo "IS YOUR PASSWORD $REPLY????"

####################################################

# read -p "Enter your name: "
# echo "hell, $REPLY"
# if read -t 5 -s -p "Enter your password: "
# then
# echo "IS YOUR PASSWORD $REPLY????"
# else
# echo "looser!"
# fi

#################################################

count=1
file="text.txt"
cat $file | while read line
do 
    echo "Line number $count is: "
    echo "$line"
    count=$(( $count + 1 ))
done
echo "Finished reading file $file"