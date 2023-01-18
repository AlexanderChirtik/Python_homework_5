import random

start_count_sweets = 201
count_sweets = start_count_sweets
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
        if (count_sweets == start_count_sweets):
            count2 = 27
            print(f'Компьютер взял следующее количество конфет {count2}')
            count_sweets -= count2
            print(count_sweets)
            first_move = 1
        else:
            count2 = max_take - count1 + 1
            print(f'Компьютер взял следующее количество конфет {count2}')
            count_sweets -= count2
            print(count_sweets)
            first_move = 1

if (first_move == 1):
    print("Победил компьютер ")
else:
    print("Вы победили ")