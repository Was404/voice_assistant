import speech_recognition
from config import commands_dict, ERROR_VOICE_UNKNOWN_VALUE, ERROR_NO_COMMAND
from colorama import Fore, Back, Style
import commands
import re
import nltk

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
            print(query)                                                
            query_without_jarvis = re.sub(r'^\s+|\s+$', '', query.replace("джарвис", ""))
            # убираем слово джарвис из ответа
            if query_without_jarvis == '': # если изначально в переменной query было только слово "джарвис", то получится пустота, избегаем этого
                listening()
            else:
                for k, v in commands_dict['commands'].items():

                    tokens = nltk.word_tokenize(query_without_jarvis) # делим предложение на токены
                    filtered_tokens = [token for token in tokens if token in v] # Фильтрация токенов на основе содержания в переменной v
                    cleaned_query = " ".join(filtered_tokens) # Создание строки из фильтрованных токенов

                    if cleaned_query in v:
                        getattr(commands, k)()
                        print(Style.BRIGHT + Back.GREEN + cleaned_query)
                        print(Style.NORMAL + Back.BLACK)
                        listening()
                        break 
                else:
                    print(Style.BRIGHT + Back.BLACK + ERROR_NO_COMMAND)
                    print(Style.NORMAL + Back.BLACK)
                    listening()                      
        else: #не прошёл проверку на джарвиса
            listening() 
    except speech_recognition.UnknownValueError:
        print(Style.DIM + ERROR_VOICE_UNKNOWN_VALUE)
        print(Style.NORMAL)
        listening()

if __name__ == '__main__':
    print(Fore.WHITE + Back.BLACK + Style.NORMAL)
    listening()
    
