import pyttsx3

engine = pyttsx3.init('sapi5') #  Microsoft Speech API для использования голоса

engine.setProperty('rate', 190) # свойства речевого движка

engine.setProperty('volume', 1.0) # свойства речевого движка

voices = engine.getProperty('voices') # получаем голос речевого движка
engine.setProperty('voice', voices[0].id)