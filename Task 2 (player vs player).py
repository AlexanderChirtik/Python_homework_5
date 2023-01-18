# 2.Создайте программу для игры с конфетами человек против человека.
import random

count_sweets = 201
max_take = 28
first_move = random.randint(0,1)
while (count_sweets != 0):
    if (first_move == 1):
        count1 = int(input("Первый игрок, возьмите конфеты "))
        if (count1 > count_sweets or count1 > max_take ):
            while (count1 > count_sweets or count1 > max_take):
                print("Вы взяли больше положенного")
                count1 = int(input("Первый игрок, возьмите конфеты "))
        count_sweets -= count1
        print(count_sweets)
        first_move = 0
    else:
        count2 = int(input("Второй игрок, возьмите конфеты "))
        if (count2 > count_sweets or count2 > max_take):
            while (count2 > count_sweets or count2 > max_take):
                print("Вы взяли больше положенного")
                count2 = int(input("Второй игрок, возьмите конфеты "))
        count_sweets -= count2
        print(count_sweets)
        first_move = 1

if (first_move == 1):
    print("Победил второй игрок ")
else:
    print("Победил первый игрок ")

# Для победы первому ходящему достаточно взять следующее количетво конфет :
# остаток от деления общего числа конфет на сумму минимального и максимального значений.
