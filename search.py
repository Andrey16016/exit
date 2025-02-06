import time
import requests
import os
from colorama import Fore

#hgrwrth4s


def bz():
    search_term = input("{+}>")
    
    file_name = 'baza.txt'
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    foundlines = [line.strip() for line in lines if search_term.lower() in line.lower()]
    if foundlines:
        print("Найденные строки:")
        for line in foundlines:
            print(line)
            print("------------------------------")
        print("Наш телеграмм: @exitbaza")
        h = input("Нажмите enter")
        exit()
    else:
        print("Ничего не найдено.")
    




def phone():
    print ("Введите номер телефона:")
    bz()

def fio():
    print ("Введите ФИО")
    bz()

def prop():
    print ("Введите Прописку:")
    bz()
    

def search():
    print ("ПОИСК ПО БАЗАМ!")
    print (Fore.GREEN + "")
    men = """
1. [Поиск по номеру]
2. [Поиск по ФИО]
3. [Поиск по прописке]
"""
    print (men)
    us = input("Выберите действе>")

    if us == "1":
        phone()
    if us == "2":
        fio()
    if us == "3":
        prop()
    
           
    

search()
