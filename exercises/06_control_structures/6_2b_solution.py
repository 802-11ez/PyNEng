#!/usr/bin/env python3
print('''
Задание 6.2b
     
Сделать копию скрипта задания 6.2a.
     
Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.
     
Ограничение: Все задания надо выполнять используя только пройденные темы.''')

print('-' * 70, '\n')
        
while True:
    ip = input('Введите IP-адрес в формате xxx.xxx.xxx.xxx: ')
    ip_l = ip.split('.')

    if len(ip_l) != 4:
        print('Wrong IP', 'IP address have more or less octets than 4.')
    elif any(oct == '' for oct in ip_l):
        print('Wrong IP', 'One or more octets is empty.')
    elif any(oct.isalpha() for oct in ip_l): 
        print('Wrong IP', 'One or more octets contains letters.') 
    elif not all(oct.isdigit() for oct in ip_l): 
        print('Wrong IP', 'One or more octets are not is digit.')
    elif any(int(oct) not in range(0,256) for oct in ip_l): 
        print('Wrong IP', 'One or more octets are not in range 0-255.') 
    else: 
        break

print('-' * 70, '\n')
if int(ip_l[0]) in range(1,224):
    print('IP address - ', ip, 'is unicast\n')
elif int(ip_l[0]) in range(224, 240):
    print('IP address - ', ip, 'is multicast\n')
elif ip == '255.255.255.255':
    print('IP address - ', ip, 'is local broadcast\n')
elif ip == '0.0.0.0':
    print('IP address - ', ip, 'is unassigned\n')
else:
    print('IP address - ', ip, 'is unused\n')
    print('-' * 70, '\n')
