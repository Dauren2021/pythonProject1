from random import randint
import operator
from secrets import choice
# . Новогодний подарок. Определить иерархию конфет и прочих сладостей.
# Создать несколько объектов-конфет. Собрать детский подарок с определением его веса. Провести сортировку конфет в подарке на основе одного
# из параметров. Найти конфету в подарке, соответствующую заданному диапазону содержания сахара
# class Sug:
#     def __init__(self,calory,chokalate,chokalatew):
#         self.cholate=chokalate
#         self.calory=calory
#         self.cholatew=chokalatew
#
#
#     def display(self):
#         print(' Name: {} '
#               ' Calory: {} '
#               ' Weight: '.format(self.calory, self.cholate, self.cholatew))
#
# s1 = Sug("Snikers", 20, 10)
# s2 = Sug("Kitkat", 30, 50)
# s3 = Sug("Twix", 20, 60)
# s4 = Sug("Bounty", 29, 68)
# s5 = Sug("Albeni", 15, 75)
# s6 = Sug("Sushniak", 55, 78)
# s = [s1, s2, s3, s4, s5, s6]
# def compute(a):
#     sumw = 0
#     count = 0
#     for i in range(a):
#         i = randint(0, 5)
#         print(s[i].calory, "weight: ", s[i].cholatew)
#         sumw += s[i].cholatew
#         if sumw > a - 50 and sumw < a:
#             break
#     print("\nWeight: ", sumw)
#
#
# while True:
#     print("Определите вес новогоднего подарка\n"
#           "1.500g  2.750g  3.1000g  4.1250g")
#     a = int(input())
#     if a == 500:
#         compute(a)
#         break
#     if a == 750:
#         compute(a)
#         break
#     if a == 1000:
#         compute(a)
#         break
#     if a == 1250:
#         compute(a)
#         break

# Камни. Определить иерархию драгоценных и полудрагоценных камней.
# Отобрать камни для ожерелья. Подсчитать общий вес (в каратах) и стоимость.
# Провести сортировку камней ожерелья на основе ценности.
# Найти камни в ожерелье, соответствующие заданному диапазону параметров прозрачности.
from random import randint

# class PreciousStone:
#     def __init__(self, name, weight, cost):
#         self.name = name
#         self.weight = weight
#         self.cost = cost
#
#     def get_info(self):
#         print(self.name, self.weight, self.cost)
#
# t1 = PreciousStone("Almaz", 1, 150000)
# t2 = PreciousStone("Rubin", 5, 100000)
# t3 = PreciousStone("Saphir", 3, 75000)
# t4 = PreciousStone("Izumrud", 6, 50000)
# t5 = PreciousStone("Gold", 2, 25000)
# t = [t1, t2, t3, t4, t5]
# def compute(a):
#     sumw = 0
#     sumc = 0
#     for i in range(a):
#         i = randint(0, 4)
#         print(t[i].name, "  ", t[i].weight, "  ", t[i].cost)
#         sumw += t[i].weight
#         sumc += t[i].cost
#     print("\nWeight: ", sumw, "\nCost: ", sumc)
#
# while True:
#     print("Alkaga kansha tas kerek tandanyz: "
#           "\n1)Almaz 2)Rubin 3)Saphir 4)Izumrud 5)Gold")
#     a = int(input("Engizu: "))
#
#     if a == 1:
#         compute(a)
#         break
#     elif a == 2:
#         compute(a)
#         break
#     elif a == 3:
#         compute(a)
#         break
#     elif a == 4:
#         compute(a)
#         break
#     elif a == 5:
#         compute(a)
#         break


# Мотоциклист. Определить иерархию амуниции. Экипировать мотоциклиста.
# Подсчитать стоимость. Провести сортировку амуниции на основе веса.
# Найти элементы амуниции, соответствующие заданному диапазону параметров цены.

file = open('venv\Objects.txt', 'w')







#import operator
# from secrets import choice
# class Motocycle:

# initte eki nizhni probel bolady tipa bylai __init__
#osynyn bfrlygyn durstap zhaz

#     def __init__(self, fullekip, weight, cost):
#         self.fullekip = fullekip
#         self.weight = weight
#         self.cost = cost
#
#     def get_info(self):
#         print('Экипировка: {}'
#               ' Вес: {}'
#               ' Цена: {}'.format(self.fullekip, self.weight, self.cost))
#
# def sort_choice(Data, choice):
#     result = sorted(Data, key=operator.attrgetter(choice))
#     for i in result:
#         i.get_info()
#
# class Amunuci(Motocycle):
#     def __init__(self, fullekip, weight, cost):
#         super().__init__(fullekip, weight, cost)
#
#
set
# moto1 = Amunuci("R2D2", 15, 35000)
# moto2 = Amunuci("COMMO", 14, 40000)
# moto3 = Amunuci("RAZOR", 10, 50000)
# moto = [moto1, moto2, moto3]

# while True:

# nau menu


#     print("1.Подсчитать стоимость экипировок")
#     print("2.Провести сортировку амуниции на основе веса")
#     print("3.Найти элементы амуниции, соответствующие заданному диапазону параметров цены")
#     print("4.exit")
#
#     a = int(input())
#
#     if a == 1:
#         sum = 0
#         for i in range(len(moto)):
#             sum += moto[i].cost
#         print("Общая сумма всех экипировок = ", sum)
#
#     if a == 2:
#         sort_choice(moto, 'weight')
#
#     if a == 3:
#         diapazon1 = int(input("Напишите диапазон цен:\n"))
#         diapazon2 = int(input())
#         for i in range(len(moto)):
#             if diapazon1 >= moto[i].cost and diapazon2 <= moto[i].cost:
#                 moto[i].get_info()
#             else:
#                 print("экипировки соответствующему диапазону отсуствует.")
#                 break
#     if a == 4:
#         break
#     if a > 4 or a < 1:
#         print("Напишите соответствующую цифру")# менюда жоқ сандар жазса осы собщ шғады

file.close()


# Таксопарк. Определить иерархию легковых автомобилей.
# Создать таксопарк. Подсчитать стоимость автопарка. Провести сортировку автомобилей
# парка по расходу топлива. Найти автомобиль в компании, соответствующий заданному диапазону параметров скорости.
# import operator
# from secrets import choice
#
#
# class Avtopark:
#     def _init_(self, model, price, raskhod_topliva, max_speed):
#         self.model = model
#         self.price = price
#         self.raskhod_topliva = raskhod_topliva
#         self.max_speed = max_speed
#
#     def show(self):
#         print('Модель: {}'
#               ' Цена: {}'
#               ' Расход топлива: {}'
#               ' Максимальная скорость: {}'.format(self.model, self.price, self.raskhod_topliva, self.max_speed))
#
#
# def sort_choice(Data, choice):
#     result = sorted(Data, key=operator.attrgetter(choice))
#     for i in result:
#         i.show()
#
#
# class Avto(Avtopark):
#
#     def __init__(self, model, price, raskhod_topliva, max_speed):
#         super()._init_(model, price, raskhod_topliva, max_speed)
#
#
# car1 = Avto('mercedes', 20000000, 3.5, 325)
# car2 = Avto('bmw', 19500000, 3.0, 320)
# car3 = Avto('audi', 15000000, 2.5, 300)
#
# e = [car1, car2, car3]
#
# while True:
#
#     print('1. Подсчитать стоимость автопарка')
#     print('2. Провести сортировку автомобилей парка по расходу топлива')
#     print('3. Найти автомобиль в компании, соответствующий заданному диапазону параметров скорости')
#     print('4. exit')
#
#     n = int(input())
#
#     if n == 1:
#         sum = 0
#         for i in range(len(e)):
#             sum += e[i].price
#         print('Общая сумма автопарка', sum)
#
#     if n == 2:
#         sort_choice(e, 'raskhod_topliva')
#
#     if n == 3:
#         diapozon1 = int(input())
#         diapozon2 = int(input())
#         for i in e:
#             if i.max_speed <= diapozon2 and i.max_speed >= diapozon1:
#                 i.show()
#
#     if n == 4:
#         break


# DECORATOR
# def timeit(func):
#     def wrapper():
#         print("hello world")
#         func()
#     return wrapper()
#
#
# @timeit
# def h():
#     print("vsem mir")


# def check(log, pas):
#     print("\nLogin : \nParol : ")
#
#     if a == a1.log and b == a1.pas:
#         print("Kerekti klienttin nomerin tandanyz: ")
#         num_id = int(input())
#         for i in range(len(k)):


# def klient(e2):
#
#     print("1.Do you want to have credit")
#     print("2. Transaction")
#     n=int(input("Your choice: "))
#
#     if n == 1:
#         while True:
#             salary=int(input("Please, enter your salary: "))
#             price=int(input("how much you want to get credit: "))
#             month=int(input("how much you want to get month: "))
#             if salary*0.35>=price//month:
#                 print("You can get credit!!!")
#                 print("Do you have this credit")
#                 print("1.Yes")
#                 print("2.No")
#                 n1=int(input())
#                 if n1==1:
#                     print("Congratulate!!!")
#                     break
#                 elif n1==2:
#                     print("Ok")

# from random import randint
# stack = []
#
#
# stack.append(-5)
# stack.append(3)
# stack.append(-4)
# stack.append(5)
# print(stack)
# stack.pop()
# print(stack)
#
# stack.append(10)
# print(stack)
# sum = 0
# for i in stack:
#     if i>0:
#         sum += i
#         print(i)
# print("summa polosh element:",sum)

# import operator
# from secrets import choice
# import datetime
#
#
# class Auth():
#     def __init__(self, log, password, name):
#         self.log = log
#         self.password = password
#         self.name = name
#
#
# class Admin(Auth):
#     def __init__(self, log, password, name):
#         super().__init__(log, password, name)
#
#     def display(self):
#         print(" Логин: {} "
#               " Пароль: {} "
#               " Имя: {} ".format(self.log, self.password, self.name))
#
#
# class Klient(Auth):
#     def __init__(self, log=None, password=None, name=None, id=None, check=None, credit=None, depozit=None, time=None,
#                  message=None):
#         super().__init__(log, password, name)
#         self.id = id
#         self.check = check
#         self.credit = credit
#         self.depozit = depozit
#         self.time = time
#         self.message = message
#
#     def display(self):
#         print(" Логин: {} "
#               " Пароль: {} "
#               " Имя: {} "
#               " ID: {} "
#               " на счету: {} "
#               " Кредит: {} "
#               " Депозит: {} "
#               " Срок: {} "
#               " Почта: {}".format(self.log, self.password, self.name, self.id, self.check, self.credit, self.depozit,
#                                   self.time, self.message))
#
#
# class Maneger(Auth):
#     def __init__(self, log, password, name):
#         super().__init__(log, password, name)
#
#     def display(self):
#         print(" Логин: {} "
#               " Пароль: {} "
#               " Имя: {} ".format(self.log, self.password, self.name))
#
#
# ##################################################################################################
# ################################################################################################## MANAGER DEF
# def manager():
#     a = input("Логин :")
#     b = input("Пароль :")
#     if a == a3.log and b == a3.password:
#         while True:
#             print("\n1.Список клиентов\n2.Кредит\n3.Депозит\n4.Сортировка\n5.Просрочка\n6.Выйти")
#             try:
#                 n = int(input("Ваш выбор :"))
#             except ValueError:
#                 print("Wrong type you are bastard!!!")
#             else:
#                 if n == 1:
#                     for i in e2:
#                         i.display()
#                 elif n == 2:
#                     for i in e2:
#                         if i.credit == "Есть":
#                             i.display()
#                 elif n == 3:
#                     for i in e2:
#                         if i.depozit == "Есть":
#                             i.display()
#                 elif n == 4:
#                     sort_choice(e2, 'name')
#                 elif n == 5:
#                     date = datetime.date.today()
#                     for i in e2:
#                         if date.day >= i.time - 7:
#                             i.display()
#                             i.message = "Срок вашего кредита приближаеться"
#                         elif date.day <= i.time - 7:
#                             i.display()
#                             i.message = "Ваш кредит просрочен"
#                 elif n == 6:
#                     break
#                 else:
#                     print("Такого варианта отсуствует, повтори еще раз: ")
#     else:
#         print("Логин или пароль неправильно")
#
#
#
# ######################################################################################  ADMIN DEF
# def admin():
#     a = input("Логин: ")
#     b = input("Пароль: ")
#     if a == a1.log and b == a1.password:
#         while True:
#             for i in e1:
#                 i.display()
#             print("1.Добавить клиента")
#             print("2.Удалить клиента")
#             print("3.Блокировать клиента")
#             print("4.Выйти в главный меню")
#             try:
#                 n = int(input("Ваш выбор: "))
#             except ValueError:
#                 print("Wrong type you are bastard!!!")
#             else:
#                 if n == 1:
#                     try:
#                         cho = int(input("Вы точно хотите добавить?\n1.Да\n2.Нет"))
#                     except ValueError:
#                         print("Wrong type you are bastard!!!")
#                     else:
#                         if cho == 1:
#                             a = Klient()
#                             e2.append(a)
#                             for i in range(1):
#                                 # self.log,self.password,self.name,self.id,self.check,self.credit,self.depozit,self.time,self.message
#                                 a.log = input("Логин: ")
#                                 a.password = input("Пароль: ")
#                                 a.name = input("Имя: ")
#                                 a.id = int(input("ID: "))
#                                 a.check = int(input("Деньги: "))
#                                 a.credit = None
#                                 a.depozit = None
#                                 a.time = None
#                                 a.message = "Вы открыли банковский счет!!!"
#                 elif n == 2:
#                     print("ID клиента: ")
#                     nID = int(input())
#                     for i in e2:
#                         if nID == i.id:
#                             cho = int(input("Вы точно хотите удалить?\n1.Да\n2.Нет"))
#                             if cho == 1:
#                                 e2.remove(i)
#                             elif cho == 2:
#                                 break
#                 elif n == 3:
#                     n1ID = int(input("Введите ID: "))
#                     for i in e2:
#                         if n1ID == i.id:
#                             cho = int(input("Вы точно хотите заблокировать?\n1.Да\n2.Нет"))
#                             if cho == 1:
#                                 i.message = "Вы заблокированы"
#                             elif cho == 2:
#                                 break
#                 elif n == 4:
#                     break
#                 else:
#                     print("Такого варианта отсуствует, повтори еще раз: ")
#     else:
#         print("Логин или пароль неправильно")
#
#
#
#
#
#
#
# ###################################################################################################### DEF SORT
# def sort_choice(Data, choice):
#     result = sorted(Data, key=operator.attrgetter(choice))
#     for i in result:
#         i.display()
#
#
# ####################################################################################################    KLIENT DEF
# def klient():
#         a = input("Логин: ")
#         b = input("Пароль: ")
#         for i in e2:
#             if a == i.log and b == i.password:
#                 i.display()
#                 while True:
#                     print("1. Брать кредит")
#                     print("2. Переводы")
#                     print("3. Выйти")
#                     try:
#                         n = int(input("Ваш выбор : "))
#                         if n == 1:
#                             salary = int(input("Пожалуйста введите свою зарплату: "))
#                             price = int(input("На сколько вы ходите брать кредит "))
#                             month = int(input("На сколько месяцев вы хотите брать кредит: "))
#
#                             if salary * 0.35 >= price // month:
#                                 print("Вы можете получить кредит!!!")
#                                 print("Вы хотите брать кредит")
#                                 print("\n1.Да \n2.Нет")
#                                 n1 = int(input("Ваш выбор :"))
#                                 if n1 == 1:
#                                     print(" Поздравляем !!!")
#                                     for i in e2:
#                                         if a == i.log and b == i.password:
#                                             i.credit = "Есть"
#                                     break
#                                 elif n1 == 2:
#                                     print("Ok")
#                                     break
#
#                         elif n == 2:
#                             try:
#                                 nID = int(input("Введите  ID: "))
#                                 nMoney = int(input("Сколько вы хотите перевести: "))
#                             except ValueError:
#                                 print("Wrong type you are bastard!!!")
#                             else:
#                                 for i in e2:
#                                     try:
#                                         cho = int(input("Вы точно хотите сделать перевод?\n1.Да\n2.Нет"))
#                                     except ValueError:
#                                         print("Wrong type you are bastard!!!")
#                                     else:
#                                         if cho == 1:
#                                             if a == i.log and b == i.password:
#                                                 i.check -= nMoney
#                                             if nID == i.id:
#                                                 i.check += nMoney
#                                                 break
#                                         elif cho == 2:
#                                             break
#
#                         elif n == 3:
#                             break
#                         else:
#                             print("Такого варианта отсуствует, повтори еще раз: ")
#
#
#
#
#
# ########################################
# #  MAIN
# a1 = Admin("admin", "1", "Tanirbergen")
# a23 = Klient("r", "7", "Ronaldo", 332, 180000, "Не имеет", "Есть", 5)
# a2 = Klient("d", "16", "Dauren", 339, 120000, "Не имеет", "Есть", 31)
# a22 = Klient("n", "20", "Nurislam", 331, 170000, "Есть", "Не имеет", 10)
# a21 = Klient("m", "0", "Merei", 330, 150000, "Есть", "Не имеет", 12)
# a3 = Maneger("m", "5", "Shavkat")
# e1 = [a1]  # Admin list
# e2 = [a21, a2, a23, a22]  # Klient list
# e3 = [a3]  # Manager list
# while True:
#     print("----------------------"
#           "\nГлавное меню:\n1.Admin\n2.Klient\n3.Manager\n4.Выйти"
#           "\n----------------------")
#     try:
#         n = int(input("Ваш выбор : "))
#     except ValueError:
#         print("Wrong type you are bastard!!!")
#     else:
#         if n == 1:
#             admin()
#         elif n == 2:
#             klient()
#         elif n == 3:
#             manager()
#         elif n == 4:
#             break
#         else:
#             print("Такого варианта отсуствует, повтори еще раз: ")
