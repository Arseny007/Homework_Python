import netifaces
import os

def netif():
    l = netifaces.interfaces()
    iface = int(input(f'Выберите интерфейс (цифра от 1 до {len(l)}): '))
    c = netifaces.ifaddresses(l[iface-1])
    print(*c.values())
    print(*netifaces.ifaddresses())
    return

netif()