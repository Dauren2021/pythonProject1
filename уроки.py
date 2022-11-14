# temperatura = -3
# if temperatura < 5:
#     print("kun salkin, kiynyp aliniz")
# else:
#     print("kun zhaksi, kidiruga bolady")
#
#
#
# month = "karasha"
# if month!= "kantar":
#     print("zhana zhil toilanbaidy")
#     print("shirsha bezendirilmeidi")
# else:
#     print("zhana zhil kutti bolsyn")
#
#
# a=5
# if a < 10:
#     print("{0} sany {1} sanynan kishi".format(a,10))
#
#
# a = 5
# b = 6
# c = 100
# if a > 4:
#     if b > a:
#         if c > b:
#             print("%2d < %2d < %2d"%(a,b,c))
#
# a = int(input("a="))
# b = int(input("b="))
# if a >= 50:
#     print("siz %d bagasymen ottiniz"%a)
# elif b >= 80 and b <= 100:
#     print("emtihannan ozi otipti birak dosynyn bagasy {}".format(a))
# else:
#     print("Baskalar da mykry emes birak siz zhazgy semestrge kaldynyz")
#



# from random import*
# a = []
# x = int(input("enter x:"))
# max=0
# ix=0
# iy=0
# for i in range(x):
#     b=randint(1,100)
#     a.append(b)
#     if max < a[i]:
#         max = a[i]
#         ix=i
# min=a[-1]
# for i in range(x):
#     if min > a[i]:
#         min = a[i]
#         iy=i
# count1 = 0
# count2=0
# print (a,"\n",min,"\n",max)
#
# if(ix<iy):
#     for ix in range(iy):
#         count1 +=1
#     print("sandar sany:", count1-1)
#
# elif(iy<ix):
#     for iy in range(ix):
#         count2 +=1
#     print("sandar sany:", count2-1)

# max = 0
# for i in range(x):
#     if i%2==0:
#         if max < a[i]:
#             max = a[i]


from random import randint
# def check(list, srez):
#     while True:
#         if len(list) == srez * srez:
#             break
#         else:
#             list.append(0)
# def tosecond(list, srez):
#     current = 0
#     mas = []
#     for i in range(srez):
#         chunk = list[current: current + srez]
#         current += srez
#         mas.append(chunk)
#     for i in mas:
#         print(i)
#
#
# s = int(input("razmer massiv = "))
# a = [randint(-50, 100) for i in range(s)]
# print(a)
# srez = int(input("bolu kerek kanshaga = "))
# check(a, 4)
# print(a)
#
# print("dvumernyi:")
# tosecond(a, srez)
# def summasiv(e, x, c):
#     sum = 0
#     suma = 0
#     sumi = 0
#     for i in range(len(e)):
#         sum += e[i]
#         suma += x[i]
#         sumi += c[i]
#     print("massivtardyn kosyndysy : ", sum , suma, sumi, sep="\n")
#
#
# a = [randint(0, 50) for i in range(7)]
# s = [randint(0, 50) for i in range(7)]
# b = [randint(0, 50) for i in range(7)]
# print(a)
# print(s)
# print(b)
# summasiv(a, s, b


# b = list("abcdefghijklmnopqrstuvwxyz")
# print(b, len(b))
# s = input("ozgeriletin soz: ")
# y = []
# q = int(input("shag: "))
# for i in s:
#   y.append(b[(b.index(i) + q) % len(b)])
# t = ''.join(y)
# print(t)


# def check(mas):
#     s=1
#     if mas[0] == "X" and mas[1] == "X" and mas[2] == "X":
#         print("player 1 win!!!")
#         return s
#     elif mas[0] == "O" and mas[1] == "O" and mas[2] == "O":
#         print("player 2 win!!!")
#         return s
#
#
#     if mas[3] == "X" and mas[4] == "X" and mas[5] == "X":
#         print("player 1 win!!!")
#         return s
#     elif mas[3] == "O" and mas[4] == "O" and mas[5] == "O":
#         print("player 2 win!!!")
#         return s
#
#     if mas[6] == "X" and mas[7] == "X" and mas[8] == "X":
#         print("player 1 win!!!")
#         return s
#     elif mas[6] == "O" and mas[7] == "O" and mas[8] == "O":
#         print("player 2 win!!!")
#         return s
#
#     if mas[0] == "X" and mas[3] == "X" and mas[6] == "X":
#         print("player 1 win!!!")
#         return s
#     elif mas[0] == "O" and mas[3] == "O" and mas[6] == "O":
#         print("player 2 win!!!")
#         return s
#
#     if mas[1] == "X" and mas[4] == "X" and mas[7] == "X":
#         print("player 1 win!!!")
#         return s
#     elif mas[1] == "O" and mas[4] == "O" and mas[7] == "O":
#         print("player 2 win!!!")
#         return s
#
#     if mas[2] == "X" and mas[5] == "X" and mas[8] == "X":
#         print("player 1 win!!!")
#         return s
#     elif mas[2] == "O" and mas[5] == "O" and mas[8] == "O":
#         print("player 2 win!!!")
#         return s
#
#
#     if mas[0] == "X" and mas[4] == "X" and mas[8] == "X":
#         print("player 1 win!!!")
#         return s
#     elif mas[0] == "O" and mas[4] == "O" and mas[8] == "O":
#         print("player 2 win!!!")
#         return s
#
#
#     if mas[2] == "X" and mas[4] == "X" and mas[6] == "X":
#         print("player 1 win!!!")
#         return s
#     elif mas[2] == "O" and mas[4] == "O" and mas[6] == "O":
#         print("player 2 win!!!")
#         return s
#     else:
#         print("eshkim utkan zhok")
# #______________________________________________
# def mashow(mas):
#     for i in range(len(mas)):
#         if i % 3 == 0 :
#             print()
#         print(mas[i], end="\t")
# #________________________________________________
# def play1(mas,a):
#     if mas[a - 1] == 'O':
#         print("Ozgermeidi baska oryndy tandanyz")
#     elif mas[a-1] == '1' or mas[a-1] == '2' or mas[a-1] == '3' or mas[a-1] == '4' or mas[a-1] == '5' or mas[a-1] == '6' or mas[a-1] == '7' or mas[a-1] == '8' or mas[a-1] == '9':
#         mas[a-1] = 'X'
#     mashow(mas)
# #_____________________________________________
# def play2(mas,a):
#     if mas[a - 1] == 'X':
#         print("Ozgermeidi baska oryndy tandanyz")
#     elif mas[a-1] == '1' or mas[a-1] == '2' or mas[a-1] == '3' or mas[a-1] == '4' or mas[a-1] == '5' or mas[a-1] == '6' or mas[a-1] == '7' or mas[a-1] == '8' or mas[a-1] == '9':
#         mas[a-1] = 'O'
#     mashow(mas)
# #_________________________________________________
# mas = ['1','2','3','4','5','6','7','8','9']
# mashow(mas)
# while True:
#     print()
#     a = int(input("Player 1 - X: \n"))
#     play1(mas, a)
#     s = check(mas)
#     if s == 1:
#         print(s)
#         break
#     print()
#     b = int(input("Player 2 - O: \n"))
#     play2(mas, b)
#     q = check(mas)
#     if q == 1:
#         print(q)
#         break


# import random
#
# num = [random.randint(0,100) for i in range(10)]
# max=0
# maxi=0
# print(num)
# for i in range(len(num)):
#     if max<num[i]:
#         max=num[i]
#         maxi=i
# print(max,maxi)print("The world's a little blurry", "Or maybe it's my eyes", end='!!!', sep=' :) ')

print("Honey, what's your hurry", end='?')

print("Told you not to worry", "But maybe that's a lie", sep=' :) ')




