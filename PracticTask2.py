#Практическое задание по теме "Переменные".
#Занание1: Количество выполненных ДЗ (запишите значение 12)
q_ty_home_task=12
#Задание2: Количество затраченных часов (запишите значение 1.5)
q_ty_hour=1.5
#Задание3: Название курса (запишите значение 'Python')
training='Python'
#Задание4: Время на одно задание (вычислить используя 1 и 2 переменные)
time_on_task=q_ty_hour/q_ty_home_task
#Задание5:Выведите на экран(в консоль), используя переменные, следующую строку:
#Курс: Python, всего задач:12, затрачено часов: 1.5, среднее время выполнения 0.125 часа.
print('Курс: '+training +
     ', всего задач: ' + str(q_ty_home_task) +
     ', затрачено часов: ' + str(q_ty_hour) +
     ', среднее время выполнения: '+ str(time_on_task) + ' часа.')
