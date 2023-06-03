import os
import subprocess as sp
from config import EXE_PATH_LOL, EXE_PATH_BROWSER
import requests
import wikipedia
import pywhatkit as kit
import sys
from email.message import EmailMessage
import smtplib
from colorama import init, Fore
from colorama import Back
from colorama import Style
#from decouple import config
from main import listening

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
    query = listening()
    kit.playonyt(query)
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
    return res["расскажи шутку"]


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['совет']['дай совет']

paths = {
    'discord': "C:\\Users\\shura\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'league of legends': "C:\\Riot Games\\Riot Client\\RiotClientServices.exe"
}

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_cmd():
    try:
        os.system('start cmd')
    except:    
        print('Указан некорректный путь')

def open_discord():
    try:
        os.startfile(paths['discord'])
    except:    
        print('Указан некорректный путь')


def open_lol():
    try:
        os.startfile(paths['league of legends'])
    except:    
        print('Указан некорректный путь')

def open_calculator():
    sp.Popen(paths['calculator'])        

def greating():
    #ПРИВЕТСТВИЕ
    print(Fore.RED + "░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗")
    print(Fore.RED + "░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝")
    print(Fore.RED + "░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░")
    print(Fore.RED + "░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░")
    print(Fore.RED + "░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗")
    print(Fore.RED + "░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝")
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
    return True
