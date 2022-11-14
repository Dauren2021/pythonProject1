
# file = open('text.txt','w', encoding='utf-8')
# file.write("Вечерело\nЖужжали мухи\nСветил фонарик\nКипела вода в чайнике\nВенера зажглась на небе\nДеревья шумели\nТучи разошлись\nЛиства зеленела")
# file.close()
# Требуется реализовать функцию longest_words(file),
# которая выводит слово, имеющее максимальную длину
# (или список слов, если таковых несколько).

def longest_words(file):
    fil = open(file, 'r', encoding='utf-8')
    s = fil.read()
    s = s.split("\n",)
    a = []
    max = 0
    for i in s:
        a.append(len(i))
    for i in a:
        if max < i:
            max = i
    for i in s:
        if max == len(i):
            print(i)

longest_words('text.txt')