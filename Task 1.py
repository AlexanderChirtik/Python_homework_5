# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input("Введите текст ").split(' ')
remove = input("Введите фрагмент ")
list = [text[i] for i in range(len(text)) if remove not in text[i]]
print(list)