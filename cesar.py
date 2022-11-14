import operator
from secrets import choice
import datetime


class Auth():
    def __init__(self, log, password, name):
        self.log = log
        self.password = password
        self.name = name


class Admin(Auth):
    def __init__(self, log, password, name):
        super().__init__(log, password, name)

    def display(self):
        print(" Логин: {} "
              " Пароль: {} "
              " Имя: {} ".format(self.log, self.password, self.name))


class Klient(Auth):
    def __init__(self, log=None, password=None, name=None, id=None, check=None, credit=None, depozit=None, time=None,
                 timeMonth=None, month=None, creditCheck=None, message=None):
        super().__init__(log, password, name)
        self.id = id
        self.check = check
        self.credit = credit
        self.depozit = depozit
        self.time = time
        self.message = message
        self.timeMonth = timeMonth
        self.month = month
        self.creditCheck = creditCheck

    def display(self):
        print(" Логин: {} "
              " Пароль: {} "
              " Имя: {} "
              " ID: {} "
              " на счету: {} "
              " Кредит: {} "
              " Депозит: {} "
              " Срок день: {} "
              " Срок месяц: {} "
              " Сколько месяц: {} "
              " Счет кредита: {} "
              " Почта: {}".format(self.log, self.password, self.name, self.id, self.check, self.credit, self.depozit,
                                  self.time, self.timeMonth, self.month, self.creditCheck, self.message))


class Maneger(Auth):
    def __init__(self, log, password, name):
        super().__init__(log, password, name)

    def display(self):
        print(" Логин: {} "
              " Пароль: {} "
              " Имя: {} ".format(self.log, self.password, self.name))


##################################################################################################
################################################################################################## MANAGER DEF
def manager():
    x = 3
    while x > 0:
        a = input("Логин :")
        b = input("Пароль :")
        if a == a3.log and b == a3.password:
            while True:
                print("\n1.Список клиентов\n2.Кредит\n3.Депозит\n4.Сортировка\n5.Просрочка\n6.Выйти")
                try:
                    n = int(input("Ваш выбор :"))
                except ValueError:
                    print("Введено неправильно, введите число")
                else:
                    if n == 1:
                        for i in e2:
                            i.display()
                    elif n == 2:
                        for i in e2:
                            if i.credit == "Есть":
                                i.display()
                    elif n == 3:
                        for i in e2:
                            if i.depozit == "Есть":
                                i.display()
                    elif n == 4:
                        sort_choice(e2, 'name')
                    elif n == 5:
                        if date.day <= i.time - 7 and i.credit == "Есть" and date.month == i.timeMonth:
                            i.display()
                            i.message = "Срок вашего кредита приближаеться"
                        elif date.day >= i.time - 7 and i.credit == "Есть" and date.month == i.timeMonth:
                            i.display()
                            i.message = "Ваш кредит просрочен"
                    elif n == 6:
                        x = 0
                        break
                    else:
                        print("Нету такого варианта, введите правильный вариант!!!")
        else:
            x -= 1
            print("Логин или пароль неправильно!!!"
                  "У вас осталось", x, "попытки"
                                       "\nВведите снова")


######################################################################################  ADMIN DEF
def admin():
    x = 3
    while x > 0:
        a = input("Логин: ")
        b = input("Пароль: ")
        if a == a1.log and b == a1.password:
            while True:
                for i in e1:
                    i.display()
                print("1.Добавить клиента")
                print("2.Удалить клиента")
                print("3.Блокировать клиента")
                print("4.Выйти в главный меню")
                try:
                    n = int(input("Ваш выбор: "))
                except ValueError:
                    print("Введено неправильноб введите число")
                else:
                    if n == 1:
                        r = '1'
                        while r == '1':
                            try:
                                cho = int(input("Вы точно хотите добавить?\n1.Да\n2.Нет"))
                            except ValueError:
                                print("Введено неправильно, введите число")
                            else:
                                r = '0'
                                if cho == 1:
                                    a = Klient()
                                    e2.append(a)
                                    for i in range(1):
                                        # self.log,self.password,self.name,self.id,self.check,self.credit,self.depozit,self.time,self.message
                                        a.log = input("Логин: ")
                                        a.password = input("Пароль: ")
                                        a.name = input("Имя: ")
                                        r = '4'
                                        while r == '4':
                                            try:
                                                a.id = int(input("ID: "))
                                            except ValueError:
                                                print("Введено неправильноб введите число")
                                            else:
                                                r = '3'
                                                while r == '3':
                                                    try:
                                                        a.check = int(input("Деньги: "))
                                                    except ValueError:
                                                        print("Введено неправильноб введите число")
                                                    else:
                                                        r = '1'
                                                        a.credit = None
                                                        a.depozit = None
                                                        a.time = None
                                                        a.message = "Вы открыли банковский счет!!!"
                                elif cho == 2:
                                    pass
                                else:
                                    print("Нету такого варианта, введите существующий")
                    elif n == 2:
                        r = '2'
                        while r == '2':
                            try:
                                print("ID клиента: ")
                                nID = int(input())
                            except ValueError:
                                print("Введено неправильно, введите ID")
                            else:
                                r = 'r'
                                for i in e2:
                                    if nID == i.id:
                                        r = 'q'
                                        while r == 'q':
                                            try:
                                                cho = int(input("Вы точно хотите удалить?\n1.Да\n2.Нет"))
                                            except ValueError:
                                                print("Введено неправильноб введите число")
                                            else:
                                                r = 'w'
                                                if cho == 1:
                                                    e2.remove(i)
                                                elif cho == 2:
                                                    break
                                                else:
                                                    print("Нету такого варианта, введите существующий")
                    elif n == 3:
                        r = 'e'
                        while r == 'e':
                            try:
                                n1ID = int(input("Введите ID: "))
                            except ValueError:
                                print("Введено неправильно, введите ID")
                            else:
                                for i in e2:
                                    if n1ID == i.id:
                                        r = 'r'
                                        while r == 'r':
                                            try:
                                                cho = int(input("Вы точно хотите заблокировать?\n1.Да\n2.Нет"))
                                            except ValueError:
                                                print("Введено неправильноб введите число")
                                            else:
                                                r = 't'
                                                if cho == 1:
                                                    i.message = "Вы заблокированы"
                                                elif cho == 2:
                                                    break
                                                else:
                                                    print("Нету такого варианта, введите существующий")
                    elif n == 4:
                        x = 0
                        break
                    else:
                        print("Нету такого варианта, введите существующий")
        else:
            x -= 1
            print("Логин или пароль неправильно!!!"
                  "У вас осталось", x, "попытки"
                                       "\nВведите снова")


###################################################################################################### DEF SORT
def sort_choice(Data, choice):
    result = sorted(Data, key=operator.attrgetter(choice))
    for i in result:
        i.display()


####################################################################################################    KLIENT DEF
def klient():
    x = 3
    while x > 0:
        a = input("Логин: ")
        b = input("Пароль: ")
        for i in e2:
            if a == i.log and b == i.password:
                i.display()
                while True:
                    print("\n\nМеню клиента\n1. Брать кредит")
                    print("2. Переводы")
                    print("3. Оплатить кредит")
                    print("4. Выйти")
                    try:
                        n = int(input("Ваш выбор : "))
                    except ValueError:
                        print("Введено неправильноб введите число")
                    else:
                        if n == 1 and i.credit == "Не имеет" and i.message != "Вы заблокированы":
                            e1 = 0
                            while e1 == 0:
                                try:
                                    salary = int(input("Пожалуйста введите свою зарплату: "))
                                except ValueError:
                                    print("Введено неправильноб введите число")
                                else:
                                    e1 = 1
                                    ee = 1
                                    while ee == 1:
                                        try:
                                            price = int(input("На сколько вы ходите брать кредит "))
                                        except ValueError:
                                            print("Введено неправильноб введите число")
                                        else:
                                            ee = 0
                                            e3 = 0
                                            while e3 == 0:
                                                try:
                                                    month = int(input("На сколько месяцев вы хотите брать кредит: "))
                                                except ValueError:
                                                    print("Введено неправильноб введите число")
                                                else:
                                                    e3 = 1
                                                    if salary * 0.35 >= price // month:
                                                        print("Вы можете получить кредит!!!")
                                                        print("Вы хотите брать кредит")
                                                        print("\n1.Да \n2.Нет")
                                                        e4 = 1
                                                        while e4 == 1:
                                                            try:
                                                                n1 = int(input("Ваш выбор :"))
                                                            except ValueError:
                                                                print("Введено неправильноб введите число")
                                                            else:
                                                                e4 = 0
                                                                if n1 == 1:
                                                                    print(" Поздравляем \n Вы получили кредит !!!")

                                                                    if a == i.log and b == i.password:
                                                                        i.credit = "Есть"
                                                                        i.creditCheck = price
                                                                        i.month = month
                                                                        i.time = date.day
                                                                        i.timeMonth = date.month + 1

                                                                elif n1 == 2:
                                                                    print("Ok")
                                                                    break
                                                                else:
                                                                    print("Нету такого варианта, введите существующий")
                                                    else:
                                                        print("Вы не можете получить кредит!!!")
                        elif n == 1 and i.credit == "Есть" and i.message != "Вы заблокированы":
                            print("У вас уже есть кредит")
                        elif n == 2 and i.message != "Вы заблокированы":
                            r = '0'
                            while r == '0':
                                try:
                                    nID = int(input("Введите  ID: "))
                                except ValueError:
                                    print("Введено неправильно, введите существующий ID")
                                else:
                                    r = '1'
                                    while r == '1':
                                        try:
                                            nMoney = int(input("Сколько вы хотите перевести: "))
                                        except ValueError:
                                            print("Введено неправильно, введите число")
                                        else:
                                            r = '3'
                                            if i.check < nMoney:
                                                print("У вас недостаточно средств для перевода!!!")
                                                break
                                            for i in e2:
                                                while r == '3':
                                                    try:
                                                        cho = int(
                                                            input("Вы точно хотите сделать перевод?\n1.Да\n2.Нет"))
                                                    except ValueError:
                                                        print("Введено неправильнo, введите число")
                                                    else:
                                                        r = '4'
                                                        if cho == 1:
                                                            if a == i.log and b == i.password:
                                                                i.check -= nMoney
                                                            if nID == i.id:
                                                                i.check += nMoney
                                                                break
                                                        elif cho == 2:
                                                            break
                                                        else:
                                                            print("Нету такого варианта, введите существующий")
                        elif n == 3 and i.message != "Вы заблокированы" and i.credit == "Есть":
                            print(i.creditCheck)
                            r = '1'
                            while r == '1':
                                try:
                                    nCreditPay = int(input("Сколько хотите заплатить"))
                                except ValueError:
                                    print("Не правильно введенный данный, "
                                          "Введите число")
                                else:
                                    r = '0'
                                    if i.creditCheck // i.month <= nCreditPay and nCreditPay <= i.check:
                                        i.creditCheck -= nCreditPay
                                        i.check -= nCreditPay
                                        i.month -= 1
                                        i.timeMonth += 1
                                        if i.creditCheck == 0:
                                            i.credit = "Не имеет"
                                            i.time = 0
                                            i.month = 0
                                            i.timeMonth = 0
                                            i.creditCheck = None
                                    elif i.creditCheck // i.month >= nCreditPay:
                                        print("Ваш месячная оплата кредита, составляет ", i.creditCheck // i.month,
                                              " tg")
                                    elif nCreditPay > i.check:
                                        print("У вас недостаточно средств для оплаты")
                        elif n == 3 and i.message != "Вы заблокированы" and i.credit == "Не имеет":
                            print("У вас нет кредита")
                        elif n == 4:
                            x = 0
                            break
                        else:
                            print("Нету такого варианта, введите существующий")
        else:
            x -= 1
            print("Логин или пароль неправильно!!!"
                  "У вас осталось", x, "попытки"
                                       "\nВведите снова")


########################################
#  MAIN
date = datetime.date.today()
a1 = Admin("admin", "1", "Tanirbergen")
a23 = Klient("r", "7", "Ronaldo", 332, 180000, "Не имеет", "Есть", 0, 0, 0)
a2 = Klient("d", "16", "Dauren", 339, 120000, "Не имеет", "Есть", 0, 0, 0)
a22 = Klient("n", "20", "Nurislam", 331, 170000, "Есть", "Не имеет", 10, date.month, 24, 500000)
a21 = Klient("m", "0", "Merei", 330, 150000, "Есть", "Не имеет", 12, date.month, 12, 1000000)
a3 = Maneger("m", "5", "Shavkat")
####################  !1
e1 = [a1]  # Admin list
e2 = [a21, a2, a23, a22]  # Klient list
e3 = [a3]  # Manager list
while True:
    print("----------------------"
          "Добро пожаловать в HALAL BANK\nГлавное меню:\n1.Admin\n2.Klient\n3.Manager\n4.Выйти"
          "\n----------------------")
    try:
        n = int(input("Ваш выбор : "))
    except ValueError:
        print("Введено неправильно, введите число")
    else:
        if n == 1:
            admin()
        elif n == 2:
            klient()
        elif n == 3:
            manager()
        elif n == 4:
            break
        else:
            print("Нету такого варианта, введите существующий")
