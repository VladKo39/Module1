#Практическое задание по уроку "Строки и индексация строк"
#Задача1 В переменную example запишите любую строку.
example='Топинамбур'
#Задача2 Выведите на экран(в консоль) первый символ этой строки.
print("Задача2: "+example[0])
#Задача3 Выведите на экран(в консоль) последний символ этой строки (используя отрицательный индекс).
print("Задача3: "+example[-1])
#Задача4 Выведите на экран(в консоль) вторую половину этой строки (С нечётным количеством символов: 'Urban' -> 'ban').
print("Задача4: "+example[5::1])
#Задача5 Выведите на экран(в консоль) это слово наоборот.
print("Задача5: "+example[::-1])
#Задача6 Выведите на экран(в консоль) каждый второй символ этой строки. (Пример: 'Топинамбур'->'оиабр')
print("Задача6: "+example[1::2])