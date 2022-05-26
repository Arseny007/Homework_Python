import os, datetime
text = os.popen("arp -a | grep wlp1s0").read()
ip_list = [line[line.find("(")+1:line.find(")")] for line in text.split("\n")][:-1]
tim = str(datetime.datetime.today())[:-10]
f = f'по состоянию на {tim} доступны: \n'
for ip in ip_list:
    f += ip + "\n"
with open('arp.log.txt', 'w') as file:
    file.write(f)