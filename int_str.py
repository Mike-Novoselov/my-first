# немного халтуры дядь Сань =)
# В данном задание мы вводим 2 числа и в ответе получеям вычитание этих чисел
a = input("Введите сколько вам лет:") # вводим число которое присваивается к символу "а"
b = input("сколько в среднем жили ваши предки:") # аналогично присваиваем число к символу "b"
c = int(b) - int(a) # вычитаем "а" и "b", используя команду int для преобразования текстового числа в численое
print(f'вам осталось жить где-то {c}') # выводим получиную информация использую "f строку" что бы получить ответ в одну строку