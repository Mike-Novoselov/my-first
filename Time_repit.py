# функция say используем для вывода в данном случае massage (текст) несолько (time) раз
def say(massage, time=1):
    print(massage * time)

say('привет')
say('Мир', 5)