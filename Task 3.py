# 3.Создайте программу для игры в ""Крестики-нолики"".

map = [1,2,3,4,5,6,7,8,9]
win_positions = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

def print_map():
    print(map[0], end=" ")
    print(map[1], end=" ")
    print(map[2])
    print(map[3], end=" ")
    print(map[4], end=" ")
    print(map[5])
    print(map[6], end=" ")
    print(map[7], end=" ")
    print(map[8])

def step_map(step, symbol):
    index = map.index(step)
    map[index] = symbol

def get_result():
    win = ""
    for i in win_positions:
        if map[i[0]] == "X" and map[i[1]] == "X" and map[i[2]] == "X":
            win = " первый игрок"
        if map[i[0]] == "O" and map[i[1]] == "O" and map[i[2]] == "O":
            win = " второй игрок"
    return win

game_over = False
player1 = True
while (game_over == False):
    print_map()
    if player1 == True:
        symbol = "X"
        step = int(input("Ход первого игрока "))
    else:
        symbol = "O"
        step = int(input("Ход второго игрока "))
    step_map(step, symbol)
    win = get_result()
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not (player1)

print_map()
print("Победил", win)