#!/usr/bin/env python3
print('''
Задание 5.1



В задании создан словарь, с информацией о разных устройствах.

Необходимо запросить у пользователя ввод имени устройства (r1, r2 или sw1).
И вывести информацию о соответствующем устройстве на стандартный поток вывода
(информация будет в виде словаря).


Пример выполнения скрипта:
    $ python task_5_1.py
    Введите имя устройства: r1
    {'location': '21 New Globe Walk', 'vendor': 'Cisco', 'model': '4451', 'ios': '15.4', 'ip': '10.255.0.1'}

Ограничение: нельзя изменять словарь london_co.

Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if.
''')

london_co = {
            'r1': {
                'location': '21 New Globe Walk',
                'vendor': 'Cisco',
                'model': '4451',
                'ios': '15.4',
                'ip': '10.255.0.1'
                },
        'r2': {
                'location': '21 New Globe Walk',
                'vendor': 'Cisco',
                'model': '4451',
                'ios': '15.4',
                'ip': '10.255.0.2'
                },
        'sw1': {
                'location': '21 New Globe Walk',
                'vendor': 'Cisco',
                'model': '3850',
                'ios': '3.6.XE',
                'ip': '10.255.0.101',
                'vlans': '10,20,30',
                'routing': True
                }
            }

hostname = input('Введите имя устройства (r1, r2, или sw1): ')

print('-' * 70, '\n')
print('Для вывода на экран требуемого по заданию словаря воспользуемся командой print()')
print('-' * 70, '\n')

print(london_co[hostname], '\n')

print('-' * 70, '\n')

print('Вывод результата на экран с помощью форматирования строк str.format()', '\n')

if hostname == 'sw1':
    template = '''
                Location   : {location}
                Vendor     : {vendor}
                Model      : {model}
                IOS        : {ios}
                IP address : {ip}
                VLANs      : {vlans}
                Routing    : {routing}
                '''
    print('-' * 70, '\n')
    print(' ' * 15, 'Hostname   :', hostname, template.format(**london_co[hostname]))
    print('-' * 70, '\n')
else:
    template = '''
                Location   : {location}
                Vendor     : {vendor}
                Model      : {model}
                IOS        : {ios}
                IP address : {ip}
                '''
    print('-' * 70, '\n')
    print(' ' * 15, 'Hostname   :', hostname, template.format(**london_co[hostname]))
    print('-' * 70, '\n')
