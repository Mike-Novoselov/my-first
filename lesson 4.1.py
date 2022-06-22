s = 'monty'
x = 'hi'
def rught_justifly(s):
    print("     "*13, s)
rught_justifly(s)
print(len(s))

print('_________________________________________________')

def do_twice (f):
    f()
    f()

def print_spam():
    print('спам')
do_twice(print_spam)
print('')

def do_twice(func, arg): # функция принемает 2 аргумента (1 функция "принт" и 1 аргумент)
    func(arg)
    func(arg)

def print_twice(arg): # функция по отображению дважды аргумента
    print(arg)
    print(arg)

def do_four(func, arg): # функция дважды вузывает функцию выше
    do_twice(func, arg)
    do_twice(func, arg)

do_twice(print, 'spam') # выполняет фунцию сфункией принт и словом спам (сама фунция ду_твайс исполняется дважды)
print('')

do_four(print, 'spam')
print('_________________________________________________')

print("+ - - - - + - - - - +")
print("|         |         |")
print("|         |         |")
print("|         |         |")
print("|         |         |")
print("+ - - - - + - - - - +")


