#!/usr/bin/env python3
import requests, subprocess, random, os, pathlib, urllib.request, pyfiglet
from datetime import datetime

def start():
    now = datetime.now()
    curdate = datetime.date(datetime.now()) ; curdate = str(curdate)
    curtime = now.strftime("%H:%M:%S")      ; curtime = str(curtime)
    otchet = ['Время запуска программы: ', curdate, curtime, '', 'Результаты выполнения программы:']
    print(pyfiglet.figlet_format("GIT EDITION"))
    print(pyfiglet.figlet_format("Ryabov M"))
    n1 = check_networkconn()    ; otchet.append(n1)
    n2 = check_firewall()       ; otchet.append(n2)
    n3 = check_firewall_work()  ; otchet.append(n3)
    n4 = check_antivirus()      ; otchet.extend(n4)
    n5 = check_av_work()        ; otchet.append(n5)
    saveotchet(otchet)
#Модуль проверки наличия соединения с Интернетом.
def check_networkconn():
    url = "http://www.google.com"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        otvet = '1. Подключено к сети Интернет.'
    except (requests.ConnectionError, requests.Timeout) as exception:
        otvet = '1. Нет сети.'
    return otvet
#Модуль проверки наличия установленного межсетевого экрана.
def check_firewall():
    fw_finder = subprocess.check_output('netsh advfirewall show currentprofile').decode("cp866")
    if 'Состояние                             ВКЛЮЧИТЬ' in fw_finder:
        otvet = '2. МЭ включен.'
    else:
        otvet = '2. МЭ отключен/отсутствует.'
    return otvet
#Модуль проверки работоспособности межсетевого экрана.
def check_firewall_work():
    weburl = urllib.request.urlopen('https://www.google.com')
    if weburl.getcode() == 200:
        data = weburl.read()
        otvet = '3. Межсетевой экран разрешил данное соединение. Является угрозой безопасности для ОС.'
    else:
        otvet = '3. МЭ прервал интернет соединение. Работает корректно.'
    return otvet
#Модуль проверки наличия установленного антивируса. поиск программы либо в реестре либо на пк
def check_antivirus():
    name1 = "C:\\Program files\\"
    name2 = ['AVAST software', 'Kaspersky', 'Eset']
    otvet = []
    for n2 in name2:
        name = name1 + n2
        if os.path.isdir(name):
            otv = '4. Установлен антивирус: '+n2+'.'
            otvet.append(otv)
    if otvet == []:
        otv = '4. Антивирусы не обнаружены!.'
        otvet.append(otv)
    return otvet
#Модуль проверки работоспособности антивирусного ПО.
def writefile(name,textgen):
    f=open(name, "w+")
    f.write(textgen)
    f.close
def check_av_work():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "[]}{()*;/,_-"
    all = lower+upper+numbers+symbols
    length = 70
    textgen = "".join(random.sample(all,length))
    name2 = "".join(random.sample(lower,5))+".txt"
    name1 = ''
    name = name1 + name2
    writefile(name,textgen)
    try:
        os.remove(name)
        otvet = '5. АВ ПО не обнаружило создание вредоносного файла '+name2+'.'
    except FileNotFoundError:
        otvet = '5. АВ ПО обнаружило создание вредоносного файла '+name2+' и отправило его в карантин.'
    except:
        otvet = '5. Неизвестная ошибка.'
    return otvet
#Модуль сохранения результатов проверки. 
def saveotchet(otchet):
    name = "Оценка Безопасности КС - Курсовая by Рябов М.txt"
    f=open(name, "w+")
    for o in otchet:
        f.write(o + '\n')
    f.close
    print('Проверка прошла успешно, результаты записаны в файл: ' + "C:\\Users\\Misha\\" + name)
start()