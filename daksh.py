
import random
import math
# #армстронг, бакытты, жай, полиндром
#
# # from random import*
# # a = []
# # x = int(input("enter x:"))
# # t = set()
# # for i in range(x):
# #
# #     a.append(randint(150, 1000000))
# #     count = 0
# #
# #     # armstrong
# #     if ((a[i] % 10) ** 3) + (((a[i] // 10) % 10) ** 3) + ((a[i] // 100) ** 3) == a[i]:
# #         print("Armstrong san: ", a[i])
# #         t.add(" Esepte Armstrong san bar")
# #
# #     # bakytty
# #     if a[i] > 100000 and ((a[i] // 1000) % 10) + ((a[i] // 10000) % 10) + (a[i] // 100000) == ((a[i] // 100) % 10) + (
# #             (a[i] // 10) % 10) + (a[i] % 10):
# #         print("Bakytty san : ", a[i])
# #         t.add(" Esepte bakytty san bar")
# #
# #     # zhai san
# #     for k in range(2, a[i]//2+1):
# #         if a[i] % k == 0:
# #             count += 1
# #     if count <= 0:
# #         print("Zhai san : ", a[i])
# #         t.add(" Esepte Zhai san bar")
# #
# #
# #     # polindrom san
# #     for w in range(x):
# #         zerk = 0
# #         e = a[i]
# #         while e > 0:
# #             q = e % 10
# #             e //= 10
# #             zerk = zerk*10 + q
# #         if a[i] == zerk:
# #             print("polinom", a[i])
# #             t.add(" Esepte polinom san bar")
# #
# #
# # print(a)
# # print(t)
#
# # from random import*
# # a = []
# # sum = 0
# # q = int(input("q = "))
# # w = int(input("w = "))
# # for i in range(q):
# #     a.append([])
# #     for k in range(w):
# #         a[i].append(randint(-50, 100))
# # for i in range(q):
# #     print(sorted(a[i]))
# # sum=0
# # for i in range(q):
# #         if k == q-(i+1):
# #             sum += a[i][k]
# # print(sum)
#
# coun = {'code': 'RU', 'name': "Russian", "population": 144}
# # coun = dict(code='RU', name="Russian")
# for key, value in coun.items():
#     print(key," - ", valu

# . Берілген мәтіннің барлық сөйлемдерін олардың әрқайсысындағы сөздер санының өсу ретімен көрсетіңіз.
# Берілген мәтіннің барлық.сөйлемдерін олардың.әрқайсысындағы сөздер санының.өсу.ретімен көрсетіңіз.
# a = []
# for i in range(10):
#      a.append(randint(-50,100))
# print(a)
# q = 0
# sum = 0
# count = 0
# for i in range(10):
#      if a[i]<0:
#           q = i
#           break
# print(q)
#
# for i in range(q):
#      sum += a[i]
#      count += 1
# print("summasy = ",sum,"\n element sany = ",count)



# # intervaldagy sandar summasy
#
#
#
# def suminter(sList):
#     sum=0
#     for i in range(5):
#         for j in range(6):
#             if sList[i][j]>=-2 and sList[i][j]<=3:
#                 sum += sList[i][j]
#                 print(sList[i][j], end=" ")
#     print("summasy = ", sum)
#
#
#
# def bolu(l, n):
#     elin = 0
#     while True:
#         bolu = l[elin: elin+n]
#         elin += n
#         if bolu:
#             yield bolu
#         else:
#             break
#
#
#
#
# b=[]
# for i in range(16):
#     b.append(random.randint(-50, 59))
# print(b)
#
# print(list(bolu(b, 4)))
#
# print("\n")
#
# a = [[random.randint(-5, 5) for i in range(6)] for j in range(5)]
# print(a)
# suminter(a)





# # ПЕРЕВЕСТИ ЧИСЛО В ДВОИЧНУЮ СИСИТЕМУ СЧИСЛЕНИЯ
# def tobin(s):
#     binnum = ''
#     while s > 0:
#         binnum = str(s % 2) + binnum
#         s //= 2
#     return binnum

# КОРТЕЖЖЖЖЖ НЕИЗМЕНЯЕМЫЙ ОБЬЕКТ

# a = 1, 2, 34
# print(a, type(a))
# for i in range(len(a)):
#     print(a[i])

# # Множество неупорядоченная колекция уникальных элементов
# a = {1, 2, 3, 4, 4, 4, 4, 5, 5, 5}
# print(a, type(a))
#
# a.add(1)
# a.update("helllo")
# b = {5,6,8,98,765,43,457}
#
# print(a & b) # ortak sandy tabu
#
# print(a | b) # eki setti kosu
# a.discard(5)
# print(a)

# # Словарь - неупорядоченная коллекция произвольных
# # обьектов с дочтупом по ключу
#
# d = {"adam""Nurislam",
#      "zat""ruchka",
#      "car""audi"
#      }
# r = dict(moskva= 495,piter=812,pqnza=13)
#
# e=[['dau','ren'],['nur','islam'],['tanir','bergen']]
# t= dict(e)
#
# q = dict.fromkeys(['a','e','r'])
#
# person={}
# s = "IVANOV IVAN Samara SGU  4 4 5 6 788 5"
# s= s.split()
# print(s)

# s = input()
# d={}
# for i in s:
#      if i in d:
#           d[i] += 1
#      else:
#           d[i]=1
# print(d)

# # zhai san
# a = int(input())
# count=0
# for k in range(2, a//2+1):
#      if a % k == 0:
#           count += 1
# if count <= 0:
#      print("Zhai san : ", a)
# else:
#      print("zhai san emes")


# # FIBONACHHI
# x1=int(input())
# x2=int(input())
# n=int(input())
# print(x1,x2,end=" ")
# while n>2:
#     x1,x2=x2,x1+x2
#     print(x2,end=" ")
#     n-=1

# # recursiv fact
# def recF(n):
#      if n==0 or n==1:
#           return 1
#      else:
#           return n*recF(n-1)

# c=5
# # for i in range(1,6):
# #     print(" " * (c),"*"*i)
# #     c -= 1
class Triangle:
    def __init__(self, a, b , c):
        self. a = a
        self. b = b
        self. c = c

    def audan(self):
        p = (self.a + self.b + self.c) /2
        s = math.sqrt(p * (p -self.a) * (p -self.b) * (p -self.c))
        return s
    def perimetr(self):
        return self.a + self.b + self.c
class Tewf:
    def i
first = Triangle(a = 10,b = 8,c = 9)
print(
    "\na1 = ",first.a,
    "\na1 = ",first.b,
    "\na1 = ",first.c,
    "\na1 = ",first.audan(),
    "\na1 = ",first.perimetr(),
)
second = Triangle(a = 36,b = 40,c = 50)
print(
    "\na1 = ",second.a,
    "\na1 = ",second.b,
    "\na1 = ",second.c,
    "\na1 = ",second.audan(),
    "\na1 = ",second.perimetr(),
)
