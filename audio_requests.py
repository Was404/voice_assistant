import pyttsx3

#RU_VOICE_ID = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\RHVoice\Anna"

tts = pyttsx3.init() #  Microsoft Speech API для использования голоса
voices = tts.getProperty('voices')

# Задать голос по умолчанию
tts.setProperty('voice', 'ru') 
# свойства речевого движка
tts.setProperty('rate', 190)
tts.setProperty('volume', 1.0) 
tts.getProperty('voices')
for voice in voices:
    if voice.name == 'Pavel' or voice.name == 'Aleksandr':
        tts.setProperty('voice', voice.id)

def say_j(msg):
    tts.say(msg)
    tts.runAndWait() #запустить на воспроизведение