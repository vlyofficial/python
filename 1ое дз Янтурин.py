a = 10
b = a + 5
number = a + b
print(number)

""""#1 задание

day = int(input("День Вашего рождения: "))
print(day)
month = int(input("Месяц Вашего рождения: "))
print(month)
name = input("Ваше имя: ")
print(name)
surname = input("Введите Вашу фамилию: ")
print(surname)"""

"""#2 задание
time = int(input("Введите время в секундах: "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print (f"Время в формате чч:мм:сс {hours} : {minutes} : {seconds}")
"""

"""#3 задание
n = int(input("Введите своё число: "))
total = (n + int(str(n) + str(n)) + int(str(n) + str(n)+str(n)))
print("Сумма чисел: {}".format(total))"""

"""#4 задание (Извините, я не понял задания)
n = int(input("Введите целое положительное число: "))"""

"""#5 задание
profits = float(input("Введите свою выручку: "))
costs = float(input("Введите свои издержки: "))
if profits > costs:
    print(f"Фирма работает с прибылью. Рентабельность {profits / costs:.2f}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника {profits / workers:.2f}")
elif profits == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма убыточная")"""

"""#5 задание
a = int(input("Введите результаты пробежки первого дня в км: "))
b = int(input("Введите общий желаемый результат в км: "))
result_days = 1
result_km = a
while result_km < b:
        a = a + a * 0.1
        result_days += 1
        result_km = result_km + a
print("Вы достигнете требуемых показателей на %.d день" % result_days)"""





















