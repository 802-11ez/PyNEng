#!/usr/bin/env python3

print('''Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

    Network:
    10        1         1         0
    00001010  00000001  00000001  00000000

    Mask:
    /24
    255       255       255       0
    11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.''')

print('-' * 70, '\n')
ip = input('Введите имя IP адрес в формате xxx.xxx.xxx.xxx/xx: ')
print('\n')
print('-' * 70, '\n')

ip_template = '''    Network:
    {0:<8} {1:<8} {2:<8} {3:<8}
    {0:08b} {1:08b} {2:08b} {3:08b}
    '''
mask_template = '''    Mask:
    /{4}
    {0:<8} {1:<8} {2:<8} {3:<8}
    {0:08b} {1:08b} {2:08b} {3:08b}
    '''
ip_l = ip.split('/')

ip_add_str = ip_l[0]
mask_str = ip_l[1]

oct1, oct2, oct3, oct4 = ip_add_str.split('.')

ip_add_int_l = [int(oct1), int(oct2), int(oct3), int(oct4)]

mask_int = int(mask_str)

ip_bin_str = '{:08b}{:08b}{:08b}{:08b}'.format(ip_add_int_l[0], ip_add_int_l[1], ip_add_int_l[2], ip_add_int_l[3])

mask_bin_str = '1' * int(mask_str) + '0' * (32 - int(mask_str))
mask_bin_l = mask_bin_str[0:8], mask_bin_str[8:16], mask_bin_str[16:24], mask_bin_str[24:]
mask_dec_l = int(mask_bin_l[0], 2), int(mask_bin_l[1], 2), int(mask_bin_l[2], 2), int(mask_bin_l[3], 2)

net_ip_bin_str = ip_bin_str[:mask_int] + '0' * (32 - mask_int)

net_ip_bin_l = net_ip_bin_str[0:8], net_ip_bin_str[8:16], net_ip_bin_str[16:24], net_ip_bin_str[24:]

net_ip_dec_l = int(net_ip_bin_l[0], 2), int(net_ip_bin_l[1], 2), int(net_ip_bin_l[2], 2), int(net_ip_bin_l[3], 2)

print(ip_template.format(net_ip_dec_l[0], net_ip_dec_l[1], net_ip_dec_l[2], net_ip_dec_l[3]))
print(mask_template.format(mask_dec_l[0], mask_dec_l[1], mask_dec_l[2], mask_dec_l[3], mask_str))
print('-' * 70, '\n')
