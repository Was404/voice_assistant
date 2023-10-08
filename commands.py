import os
import subprocess as sp
import requests
import wikipedia
import pywhatkit as kit
import sys
import re
from email.message import EmailMessage
import smtplib
from colorama import init, Fore
from colorama import Back
from colorama import Style
#from decouple import config
from main import listening
import audio_requests as ar
import getpass

username = getpass.getuser()
#EMAIL = config("EMAIL")
#PASSWORD = config("PASSWORD")

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]


def search_on_wikipedia():
    query = listening()
    results = wikipedia.summary(query, sentences=4) # кол-во предложений из вики
    return results


def play_on_youtube():
    print('Что хотите посмотреть?')
    ar.say_j('Что хотите посмотреть?')
    query = listening()
    kit.playonyt(query)
    ar.say_j('Запрос выполнен')
    return 'Запрос выполнен'


def search_on_google():
    print('Что загуглить?')
    query = listening()
    kit.search(query)
    return 'Запрос выполнен'


def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+7{number}", message) # метод для отправки сообщения WhatsApp


#def send_email(receiver_address, subject, message):
#    try:
#        email = EmailMessage()
#        email['To'] = receiver_address
#        email["Subject"] = subject
#        email['From'] = EMAIL
#        email.set_content(message)
#        s = smtplib.SMTP("smtp.gmail.com", 587)
#        s.starttls()
#        s.login(EMAIL, PASSWORD)
#        s.send_message(email)
#        s.close()
#        return True
#    except Exception as e:
#        print(e)
#        return False
    

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    ar.say_j(res["расскажи шутку"])
    return res["расскажи шутку"]


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    ar.say_j(res['совет']['дай совет'])
    return res['совет']['дай совет']

paths = {
    'discord': f"C:\\Users\\{username}\\AppData\\Local\\Discord\\app-1.0.9013\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'league of legends': "D:\Riot Games\Riot Client\RiotClientServices.exe",
    'steam' : "C:\Program Files (x86)\Steam\steam.exe"
}

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_cmd():
    try:
        os.system('start cmd')
    except:    
        print('Указан некорректный путь')
        ar.say_j('ой ой')


def open_discord():
    try:
        os.startfile(paths['discord'])
    except:    
        print('Указан некорректный путь')
        ar.say_j('Указан некорректный путь к приложению')


def close_discord():
    try:
        os.close(paths['discord'])
    except:    
        print('Указан некорректный путь')
        ar.say_j('Указан некорректный путь к приложению')


def open_lol():
    try:
        os.startfile(paths['league of legends'])
    except:    
        print('Указан некорректный путь')
        ar.say_j('Указан некорректный путь к приложению')


def open_calculator():
    sp.Popen(paths['calculator']) 


def find_exe_files():
    print('Продиктуйте, пожалуйста, названия программ')
    ar.say_j('Пожалуйста, продиктуйте названия программ')
    path_list = listening()
    found_files = []
    for path in path_list:
        for root, dirs, files in os.walk(path):
            for file_name in files:
                if file_name.endswith('.exe'):
                    found_files.append(os.path.join(root, file_name))
                    print(f"Найдено: {found_files}")
    ar.say_j(f"Я нашёл следующее: {found_files}")
    return found_files


def open_steam():
    try:
        os.startfile(paths['steam'])
    except:    
        print('Указан некорректный путь')
        ar.say_j('Указан некорректный путь к приложению')


def count_functions():
    # открываем текущий файл на чтение
    with open(__file__, "r") as f:
        # читаем содержимое файла в строку
        content = f.read()
        # ищем все функции в строке с помощью регулярки
        functions = re.findall(r"def\s+(\w+)\s*\(", content)
        # выводим количество функций и их названия в алфавитном порядке
        k = len(functions)
        print("Количество команд: ", k)
        print("Названия команд:")
        for func in sorted(functions):
            print("-", func)
    ar.say_j(f"Количество моих комманд {k}")
    ar.say_j("Я вывел список команд.")        


def greating():
    #ПРИВЕТСТВИЕ
    ar.say_j(f'Здравствуйте {username}!А вы не плохо выглядите сегодня')
    print(Fore.RED + "██╗░░██╗███████╗██╗░░░░░██╗░░░░░░█████╗░ ██╗")
    print(Fore.RED + "██║░░██║██╔════╝██║░░░░░██║░░░░░██╔══██╗ ██║")
    print(Fore.RED + "███████║█████╗░░██║░░░░░██║░░░░░██║░░██║ ██║")
    print(Fore.RED + "██╔══██║██╔══╝░░██║░░░░░██║░░░░░██║░░██║ ╚═╝")
    print(Fore.RED + "██║░░██║███████╗███████╗███████╗╚█████╔╝ ██╗")
    print(Fore.RED + "╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝░╚════╝░ ╚═╝")
    print(Fore.WHITE + "")


def stop_jarvis():
    print(Fore.RED + "██████╗░██╗░░░██╗███████╗██╗")
    print(Fore.RED + "██╔══██╗╚██╗░██╔╝██╔════╝██║")
    print(Fore.RED + "██████╦╝░╚████╔╝░█████╗░░██║")
    print(Fore.RED + "██╔══██╗░░╚██╔╝░░██╔══╝░░╚═╝")
    print(Fore.RED + "██████╦╝░░░██║░░░███████╗██╗")
    print(Fore.RED + "╚═════╝░░░░╚═╝░░░╚══════╝╚═╝")
    print(Fore.WHITE + "")
    sys.exit()