#!/bin/bash

ip2int()
{
    local a b c d
    { IFS=. read a b c d; } <<< $1
    echo $(((((((a << 8) | b) << 8) | c) << 8) | d))
}
int2ip()
{
    local ui32=$1; shift
    local ip n
    for n in 1 2 3 4; do
        ip=$((ui32 & 0xff))${ip:+.}$ip
        ui32=$((ui32 >> 8))
    done
    echo $ip
}
netmask()
# Example: netmask 24 => 255.255.255.0
{
    local mask=$((0xffffffff << (32 - $1))); shift
    int2ip $mask
}
broadcast()
# Example: broadcast 192.0.2.0 24 => 192.0.2.255
{
    local addr=$(ip2int $1); shift
    local mask=$((0xffffffff << (32 -$1))); shift
    int2ip $((addr | ~mask))
}
network()
# Example: network 192.0.2.0 24 => 192.0.2.0
{
    local addr=$(ip2int $1); shift
    local mask=$((0xffffffff << (32 -$1))); shift
    int2ip $((addr & mask))
}

echo "Привет, это bash script - ip calc"
while true; do
    echo "Что желаешь получить? пожалуйста, нажми цифру и Enter."
    echo "1) маску из цифры от 0 до 32"
    echo "2) свои ip адрес и сеть"
    echo "3) свой внешний белый ip адрес"
    echo "4) адрес сети, бродкаст, минимальный и максимальный ip адреса по ip адресу и маске"
    echo "5) чтобы выйти"
    read answer
    case $answer in
        1) echo "введи цифру от 0 до 32 чтобы увидеть маску"
        read mask
        echo $(netmask $mask) ;;
        2) ip=$(ip a s wlp1s0 | grep "inet " | cut -c 9- | cut --complement -d " " -f 1 | cut -d " " -f 1)
        { IFS=/ read addr mask; } <<< $ip
        netaddr= $(network $addr $mask)
        echo "Твои адрес, маска и сеть:" $addr $netaddr $mask ;;
        3) echo "Твой внешний адрес" $(curl -s ifconfig.me/ip) ;;
        4) echo "введи адрес и маску (0-32) для расчета через пробел"
          read addr mask
          netaddr=$(network $addr $mask)
          broadaddr=$(broadcast $addr $mask)
          echo "адрес сети: " $netaddr
          echo "бродкаст: " $broadaddr
          { IFS=. read a b c d; } <<< $broadaddr
          maxaddr=$a"."$b"."$c"."$(( $d - 1 ))
          { IFS=. read a b c d; } <<< $netaddr
          minaddr=$a"."$b"."$c"."$(( $d + 1 ))
          echo "минимальный адрес(шлюз): " $minaddr
          echo "максимальный адрес: " $maxaddr
          echo "максимальное количество хостов:" $(((2**$((32-$mask))-2))) ;;
        5) echo "goodbye"
          break ;;
        *) echo "Упс, неправильный ввод, пожалуйста, попробуй ещё раз" ;;
    esac

done
