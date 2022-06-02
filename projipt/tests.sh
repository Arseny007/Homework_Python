#!/bin/bash

#bra="Hello, World!"
#res=""
#{ IFS=" " read -a res; } <<< "$bra"
##for word in $res; do
##    echo $word
##done
#echo ${word[0]}
#echo ${word[1]}
#
ip2int()
{
    local a b c d
    { IFS=. read a b c d; } <<< $1
    echo $(((((((a << 8) | b) << 8) | c) << 8) | d))
}

ip=$(ip a s wlp1s0 | grep "inet " | cut -c 9- | cut --complement -d " " -f 1 | cut -d " " -f 1)
echo $ip
