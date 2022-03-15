import msvcrt
PLAYER_START_X = 3
PLAYER_START_Y = 3
PLAYER_ICON = 0
player = {
    "name": "Player",
    "health": 1000,
    "armor": 50,
    "damage": 10,
    "pos_x": PLAYER_START_X,
    "pos_y": PLAYER_START_Y,
    "icon": PLAYER_ICON
}

item = {
    "name": "Player",
    "health": 1000,
    "armor": 50,
    "damage": 10,
    "pos_x": PLAYER_START_X,
    "pos_y": PLAYER_START_Y,
    "icon": PLAYER_ICON
}


def step_direction(player, input_char):

    while True:
        if input_char.upper() == 'W':
            if player["pos_x"] == 1:
                break
            else:
                player["pos_x"] = player["pos_x"] - 1
                break
        elif input_char.upper() == 'S':
            if player["pos_x"] == 18:
                break
            else:
                player["pos_x"] = player["pos_x"] + 1
                break
        elif input_char.upper() == 'A':
            if player["pos_y"] == 1:
                break
            else:
                player["pos_y"] = player["pos_y"] - 1
                break
        elif input_char.upper() == 'D':
            if player["pos_y"] == 28:
                break
            else:
                player["pos_y"] = player["pos_y"] + 1
                break
        else:
            print("not correct move")
            print('step direction')
            input_char = msvcrt.getwch()


def step_on_item(player, item):

    if player["pos_x"] == item["pos_x"] and player["pos_y"] == item["pos_y"]:
        # funkcja pobierająca item
        print("dupa")


def step_on_monster(player, monster):

    if player["pos_x"] == monster["pos_x"] and player["pos_y"] == monster["pos_y"]:
        # tryb walki
        print("monster")
