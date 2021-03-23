import json
import string
#алфавиты (латиница и кириллица)
alfavit = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
alfavit_lat = string.ascii_lowercase
numbers = '0123456789'
#латиница + арабские цифры
alf_upgrade = numbers + alfavit_lat
with open('C:\\Users\spams\Downloads\\medium.txt', 'r', encoding = 'utf-8') as f:
    a = f.read()
#список букв в тексте
fr = [i for i in a if i in alf_upgrade]
#кол-во букв в тексте
d = {}
for i in fr:
    d[i] = d.get(i,0) + 1
#ранжированный список букв по их кол-ву в тексте
sorted_values = sorted(d.values(),reverse=True)
sorted_d = {}
for i in sorted_values:
    for k in d:
        if d[k] == i:
            sorted_d[k] = i
letters = [i for i in sorted_d]
print('letters:', letters)
#буквы кириллицы в порядке их частоты используемости в тексте
kir = 'оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфъ'
letters_k = [i for i in kir]
#буквы латиницы в порядке их частоты используемости в тексте
letters_l = 'etaonrishdlfcmugypwbvkxjqz'
letters_l = [i for i in letters_l]
print('letters_l:', letters_l)
#создаем словарь где ключ - это "старая" буква, а значение - "новая". Далее используем его для замены букв в тексте
notepad = {}
for i in range(29):
    if i < 26:
        notepad[letters[i]] = letters_l[i]
    else:
        notepad[letters[i]] = letters[i].upper()
print('notepad:', notepad)

#замена "неправильных" букв на "правильные"
b = ''
for i in range(len(a)):
    if a[i] in notepad:
        if a[i] == 'h':
            b += 'u'
        elif a[i] == 'k':
            b += 'f'
        elif a[i] == '6':
            b += 'h'
        elif a[i] == 'm':
            b += 'i'
        elif a[i] == '2':
            b += 'n'
        elif a[i] == '9':
            b += 'w'
        elif a[i] == 'w':
            b += 'm'
        elif a[i] == 'x':
            b += 'r'
        elif a[i] == 'z':
            b += 'l'
        elif a[i] == 'f':
            b += 'c'
        elif a[i] == 'y':
            b += 'y'
        elif a[i] == '7':
            b += 'p'
        elif a[i] == '8':
            b += 'd'
        elif a[i] == 'e':
            b += '4'
        elif a[i] == 'i':
            b += '5'
        elif a[i] == 't':
            b += 'j'
        elif a[i] == 'l':
            b += 'q'
        elif a[i] == 'n':
            b += 'x'
        else:
            b += notepad[a[i]]
    else:
        b += a[i]
print(b)

#передача дешифрованного текста в новый файл
with open('C:\\Users\spams\Downloads\\medium_answer.txt', 'w', encoding = 'utf-8') as w:
    w.write(b)
