'''

"#Задание_1
def my_func(*args):
    try:
        arg1 = int(input("Input first argument: "))
        arg2 = int(input("Input second argument: "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Wrong! You can't use zero as an argument"

    return res
print(f'result  {my_func()}')
'''

'''
#Задание_2
name = input('enter name: ')
surname = input('enter surname: ')
year = int(input('enter year: '))
city = input('enter city: ')
email = input('enter email: ')
telephone = input('input telephone: ')

def my_func (name, surname, year, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])
print(my_func(name='Vladislav',surname='Yanturin',year='1996',city='Moscow',email='ianturin@yandex.ru',telephone='89775014661'))
'''

'''
#Задание_3
def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Result - {my_func(int(input("enter first argument ")), int(input("enter second argument ")), int(input("enter third argument ")))}')
'''

'''#Задание_4
def my_func(x, y):
    return 1 / x ** abs(y)
    #return x ** y
print(my_func(2, -3))
'''

'''#Задание_5
def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Input numbers or Q for quit - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Current sum is {sum_res}')
    print(f'Your final sum is {sum_res}')


my_sum()
'''

'''#Задание_6
def int_func (*args):
    word = input("Input words ")
    print(word.title())
    return
int_func() 
'''


