import speech_recognition
from config import commands_dict, ERROR_VOICE_UNKNOWN_VALUE, ERROR_NO_COMMAND
import audio_requests as ar
from colorama import Fore, Back, Style
import commands
import re
import g4f

#nltk.download('punkt')

def it_jarvis(query):
    return "джарвис" in query.replace(" ", "") #Вернёт тру или фолс

def listening():
    print("Listening...")
    try:
        sr = speech_recognition.Recognizer()
        sr.pause_threshold = 0.5
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5) # уровень шума
            audio = sr.listen(source=mic) #слушает
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower() #получаем на вход    
        if it_jarvis(query): #полученный ответ кидаем на проверку
            #ar.say_j("Слушаю вас")
            print(f"Принял фразу:{query}")                                                
            query_without_jarvis = re.sub(r'^\s+|\s+$', '', query.replace("джарвис", ""))
            # убираем слово джарвис из ответа
            if query_without_jarvis == '': # если изначально в переменной query было только слово "джарвис", то получится пустота, избегаем этого
                listening()
            else:
                for k, v in commands_dict['commands'].items():
                    if query_without_jarvis in v:
                        print(f"Running command {k}!")
                        ar.say_j(f"Выполняю команду {query_without_jarvis}")
                        getattr(commands, k)()
                        print(Style.BRIGHT + Back.GREEN + query_without_jarvis)
                        print(Style.NORMAL + Back.BLACK)
                        listening()
                        break
                    else:
                        response = g4f.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role": "user", "content": query_without_jarvis}],stream=True,)
                        response_ls = []
                        for message in response:
                            print(message, flush=True, end='')
                            response_ls.append(message) 
                        response_ls = ''.join(response_ls)      
                        ar.say_j(response_ls)
                        print(Style.BRIGHT + Back.BLACK + ERROR_NO_COMMAND)
                        print(Style.NORMAL + Back.BLACK)
                        listening()                      
        else: #не прошёл проверку на джарвиса
            listening()
            return query 
    except speech_recognition.UnknownValueError:
        print(Style.DIM + ERROR_VOICE_UNKNOWN_VALUE)
        print(Style.NORMAL)
        listening()

if __name__ == '__main__':
    print(Fore.RED + "░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗░░░██████╗██╗██████╗░")
    print(Fore.RED + "░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝░░██╔════╝██║██╔══██╗")
    print(Fore.RED + "░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░░╚█████╗░░██║██████╔╝")
    print(Fore.RED + "░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░░░░╚═══██╗██║██╔══██╗")
    print(Fore.RED + "░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗░░██████╔╝██║██║░░██║")
    print(Fore.RED + "░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝░░╚═════╝░╚═╝╚═╝░░╚═╝")
    print(Fore.WHITE + "")
    ar.say_j('Готов к работе!')
    print(Fore.WHITE + Back.BLACK + Style.NORMAL)
    listening()
    