import string
with open(file, 'r', encoding = 'utf-8') as f:
    a = f.read(107)
    b = f.read(95)
print(a)
print(b)
print('_______________________________________________________________________________________________________________')
alfavit = string.ascii_lowercase
numbers = '0123456789'
#алфавит + цифры
alfavit_upgrade1 = alfavit + numbers
alfavit_upgrade2 = numbers + alfavit
print('alfavit_upgrade2:', alfavit_upgrade2)
nominal = {}
for i in range(26):
    nominal[alfavit[i]] = i
nominal1 = {}
for i in range(36):
    nominal1[alfavit_upgrade1[i]] = i
nominal2 = {}
for i in range(36):
    nominal2[alfavit_upgrade2[i]] = i
print('nominal2:', nominal2)
#кириллица
kir = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
# nominal1['a'] = 22
# print(nominal1['a'])
print('_______________________________________________________________________________________________________________')
# вывод текста со всеми возможными сдвигами
for j in range(33):
    a_new = ''
    for i in range(len(a)):
        if a[i] in alfavit_upgrade1:
            a_new += kir[nominal1[a[i]]+j]
        elif a[i] == ' ':
            a_new += ' '
    print(a_new)
    b_new = ''
    for i in range(len(b)):
        if b[i] in alfavit_upgrade1:
            b_new += kir[nominal1[b[i]]+j]
        elif b[i] == ' ':
            b_new += ' '
    print(b_new)
    print('_______________________________________________________________________________________________________________')
'''
возможные буквы:

устойчивые выражения:

'''
