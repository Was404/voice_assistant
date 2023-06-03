EXE_PATH_LOL = 'commands\LOL\ahk\Open lol.exe'
EXE_PATH_BROWSER = 'commands\browser\ahk\Run browser.exe'

ERROR_NO_COMMAND = 'У меня нет такой команды, но я продолжу вас слушать'
ERROR_VOICE_UNKNOWN_VALUE = 'Проблема с распознаванием речи'

commands_dict = {
    'commands': {
        'greating' : ['привет', 'здравствуйте', 'эй', 'меня слышно', 'здравствуй'],
        'open_lol' : ['запусти лигу', 'включи лигу', 'включи лигу легенд', 'запусти лол'],
        'search_on_google' : ['запусти браузер', 'открой браузер', 'включи браузер', 'загугли'],
        'open_camera' : ['открой камеру', 'запусти камеру', 'камера'],
        'open_cmd' : ['открой консоль', 'запусти консоль', 'консоль', 'цмд'],
        'open_discord' : ['открой дискорд', 'запусти дискорд', 'дискорд', 'открой discord'],
        'find_my_ip' : ['мой айпи адрес', 'мой айпи', 'ip адрес', 'ip'],
        'open_calculator' : ['открой калькулятор','запусти калькулятор', 'калькулятор'],
        'stop_jarvis' : [ 'закругляйся', 'выключись', 'отключись', 'замолчи', 'стоп']
    }
}