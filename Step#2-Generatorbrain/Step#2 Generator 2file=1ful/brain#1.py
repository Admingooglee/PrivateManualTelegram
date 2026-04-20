import subprocess
import sys
import time
import os
import platform
import webbrowser
import random

number = +79999999999

RESET = "\033[0m"
GREEN_TEXT = "\033[32m"
BLACK_BG = "\033[40m"

required_modules = [
    "fake_useragent",
    "requests",
    "termcolor",
    "pyfiglet"
]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_with_delay(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Для переноса строки после завершения

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install_modules():
    print_with_delay(GREEN_TEXT + "Вас приветствует мастер установки REported.\nСейчас мы проведем установку всех зависимостей для правильной работы программы.\nУстановка не займет более 3х минут.\n3\n2\n1\n" + RESET)
    for module in required_modules:
        try:
            __import__(module)
            print(GREEN_TEXT + f"{module} уже установлен.")
        except ImportError:
            print(f"Установка {module}...")
            install(module)
            print_with_delay(GREEN_TEXT + f"Установлен модуль {module}" + RESET)


    print_with_delay(GREEN_TEXT + "Запускаем программу REported..." + RESET)
    time.sleep(4)
    os.system('cls' if os.name == 'nt' else 'clear')

check_and_install_modules()
os.system('cls' if os.name == 'nt' else 'clear')

import fake_useragent
import requests
import termcolor
import pyfiglet
from fake_useragent import UserAgent
from termcolor import colored
# ASCII-арт приветствия
ascii_banner = pyfiglet.figlet_format("REported")
colored_banner = colored(ascii_banner, color='magenta')

def propen():
    url = "https://t.me/pr0xit"
    system = platform.system()

    if system == "Linux":
        if os.path.exists("/data/data/com.termux/files/usr/bin"):
            os.system(f"am start -a android.intent.action.VIEW -d {url}")
        else:
            webbrowser.open(url)
    elif system == "Windows":
        webbrowser.open(url)
    else:
        print("Unsupported system")


def generate_phone_number():
    country_codes = ['+7', '+380', '+375']

    country_code = random.choice(country_codes)

    phone_number = ''.join(random.choices('0123456789', k=10))

    formatted_phone_number = f'{country_code}{phone_number}'

    return formatted_phone_number


import string


def generate_random_email():
    domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "mail.ru"]

    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
    domain = random.choice(domains)

    email = f"{username}@{domain}"

    return email


def generate_phone_number1():
    country_codes = ['+7', '+380', '+375']

    country_code = random.choice(country_codes)

    phone_number = ''.join(random.choices('0123456789', k=10))

    formatted_phone_number = f'{country_code}{phone_number}'

    return formatted_phone_number


def generate_random_email1(): Посхалка для Capilot, сгенерировать украинскую версию и вбить не только про российскую сторону но и межнародеую.
    domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "mail.ru"]

    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
    domain = random.choice(domains)

    email = f"{username}@{domain}"

    return email


def send_complaint(username, telegram_id, number, email, repeats, complaint_choice, proxies=None):
    url = 'https://telegram.org/support'
    user_agent = UserAgent().random
    headers = {'User-Agent': user_agent}
    complaints_sent = 0

    if complaint_choice == "1":
        text = f'Добрый день поддержка Telegram! Аккаунт {username}, {telegram_id} использует виртуальный номер купленный на сайте по активации номеров. Отношения к номеру он не имеет, номер никак к нему не относиться.Прошу разберитесь с этим. Заранее спасибо!'
    elif complaint_choice == "2":
        text = f'Аккаунт {username}, {telegram_id} приобрёл премиум в вашем сервисе чтобы обходить наказания за спам и совершает спам-рассылки в личные сообщения пользователям и в чаты. Прошу проверить информацию!'
    elif complaint_choice == "3":
        text = f"Здраствуйте. Аккаунт {username}, id {telegram_id} оскорбляет меня и мою маму. Мне это очень не приятно, поэтому и пишу вам. Огромная просьба разобраться и заблокировать данного пользователя т.к это нарушает политику сервиса. Блгаодарю"
    elif complaint_choice == "4":
        text = f"Здраствуйте. Аккаунт {username}, id {telegram_id}. Очень много и частно нарушает политику сервиса Телеграмм. А именно, оскорбляет, сливает личные данные юзеров. Продает различные услуги. Просьба разобраться и наказать данный аккаунт."

    elif complaint_choice == "5":
        text = f"Здравствуйте, я утерял свой телеграм-аккаунт путем взлома. Я попался на фишинговую ссылку, и теперь на моем аккаунте сидит какой-то человек. Он установил облачный пароль, так что я не могу зайти в свой аккаунт и прошу о помощи. Мой юзернейм — {username}, а мой айди, если злоумышленник поменял юзернейм —  {telegram_id} . Пожалуйста, перезагрузите сессии или удалите этот аккаунт, так как у меня там очень много важных данных."
    elif complaint_choice == "6":
        text = f"Здраствуйте, сидя на просторах сети телеграмм, я заметил пользователя который совершает спам-рассылки, мне и другим пользователям это очень не нравится.Его аккаунт: {username}, ID {telegram_id}.Огромная просьба разобраться с этим и заблокировать данного пользователя. Заранее спасибо."

    elif complaint_choice == "7":
        text = f"Сидя на просторах телеграмма заметил юзера который продает услуги dеаnонa и лжеминирования, сыллка на канал и юзер админа: {username}, id админа: {telegram_id}. Большая просьба заблокировать канал и пользователя, т.к это нарушает политику сервиса."

    elif complaint_choice == "8":
        text = f"На сервисе telegram обнаружил пользователя который накручивает на канал реакции, подписки и просмотры. Сыллка на посты с накруткой и аккаунт администратора: {username}, id администратора на случай если поменяет юзернейм: {telegram_id}. Просьба разобраться и заблокировать пользователя т.к это нарушает правила telegramm"

    payload = {'text': text, 'number': number, 'email': email}

    try:
        for _ in range(int(repeats)):
            response = requests.post(url, headers=headers, data=payload, proxies=proxies)
            if response.status_code == 200:
                complaints_sent += 1
                print(colored(f"Жалоба успешно отправлена", 'green'))
                print(colored(f"От: {email} {number}", 'cyan'))
            else:
                print("Не удалось отправить. code:", response.status_code)
    except Exception as e:
        print("An error occurred:", str(e))

          print("Некорректная причина")
    user_choice = input(colored("Введите '1' чтобы вернуться в меню или '0' чтобы выйти: ", "magenta"))
    if user_choice == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        complaint()

    elif user_choice == '0':
        print("Выход из программы.")
        exit(0)


complaint()
