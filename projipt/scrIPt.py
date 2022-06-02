import ipaddress
import os

hello = """\nЧто желаешь получить? пожалуйста, нажми цифру и Enter.)
    1) маску из цифры от 0 до 32
    2) свои ip адрес и сеть
    3) свой внешний белый ip адрес
    4) адрес сети, бродкаст, минимальный и максимальный ip адреса по ip адресу и маске
    5) чтобы выйти"""
print("Привет, это Python script - ip calc")
while True:
    print(hello)
    ans = input()
    if ans == "1":
        ipaddr = ipaddress.IPv4Network(f"0.0.0.0/{input('введи цифру от 0 до 32 чтобы увидеть маску: ')}")
        print("\nмаска: ", ipaddr.netmask)
    elif ans == '2':
        just_ip = os.popen('ip a s wlp1s0 | grep "inet " | cut -c 9- | cut --complement -d " " -f 1 | cut -d " " -f 1').read()[:-1]
        yoip = ipaddress.IPv4Network(just_ip, False)
        print("\nТвои адрес, маска и сеть:", *just_ip.split("/"), yoip.network_address)
    elif ans == '3':
        print("\nтвой внешний ip: ", os.popen("curl -s ifconfig.me/ip").read())
    elif ans == '4':
        text = input("Введи адрес и маску для расчета через пробел: \n")
        addr, mask = text.split(' ')
        netw = ipaddress.IPv4Network(text.replace(' ', '/'), False)
        netaddr, broadaddr = netw.network_address, netw.broadcast_address
        print("Адрес сети: ", netaddr)
        print("Бродкаст: ", broadaddr)
        print("Минимальный адрес: ", ipaddress.IPv4Address(netaddr)+1)
        print("Минимальный адрес: ", ipaddress.IPv4Address(broadaddr)-1)
        print("максимальное количество хостов: ", str(2**(32-int(mask))-2))
    elif ans == '5':
        break


