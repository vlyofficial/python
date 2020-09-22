'''
#1 Задание
my_int = 2
my_float = 3.5
my_str = "Привет, Олимпийский"
my_list = ["i", "75", "26"]
my_tuple = ("n", "4", "6")
my_dict = {"food": "Pizza", "drink": "Cola"}
own_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in own_list:
    print(f"{i} is {type(i)}")
'''

'''
#2 Задание
my_list = ["а", "б", "в", "г", "д", "е"]
if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        el = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = el
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
print(my_list)'''

'''
#3 задание
number = int(input("Введите номер месяца: "))
if number <= 12 and number >= 1:
    month_dict = {1: "Январь",
                  2: "Февраль",
                  3: "Март",
                  4: "Апрель",
                  5: "Май",
                  6: "Июнь",
                  7: "Июль",
                  8: "Август",
                  9: "Сентябрь",
                  10: "Октябрь",
                  11: "Ноябрь",
                  12: "Декабрь"}
    month_list = list(month_dict.values())
    for i, el in enumerate(month_list):
        if i == number-1:
            print(f"Месяц из листа: {month_list[i]}")
            break
    print(f"Месяц из словаря: {month_dict[number]}")
else:
    print("Вы допустили ошибку")
    '''

'''
#4 Задание
my_str = input("Введите строку: ")
a = my_str.split(' ')
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. - {el}")
'''

'''
#5 Задание
number = int(input("Enter number: "))
my_list = [10, 5, 6, 4]
c = my_list.count(number)
for element in my_list:
    if c > 0:
        i = my_list.index(number)
        my_list.insert(i+c, number)
        break
    else:
        if number > element:
            j = my_list.index(element)
            my_list.insert(j, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)
'''