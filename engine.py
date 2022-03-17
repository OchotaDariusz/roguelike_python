import random
import winsound
import battlePhase
import HeroAndMonsters
import winsound
import util

mercenary = HeroAndMonsters.mercenary
infantry_of_Troy = HeroAndMonsters.infantry_of_Troy
cavalry_of_Troy = HeroAndMonsters.cavalry_of_Troy
enemy_hero = HeroAndMonsters.enemy_hero

GATE_SYMBOLS = {
    "up": "^",
    "down": "V",
    "left": "<",
    "right": ">"
}

ITEM_NAME = 0
ITEM_TYPE = 1
ITEM_DAMAGE = 2
ITEM_DEFENSIVE = 3
ITEM_HEALTH = 4


def create_board(width, height):
    board = []
    gates_coordinates_x, gates_coordinates_y = get_gates_coordinates(
        width, height)
    for row_number in range(height):
        row_line = []
        for col_number in range(width):
            if row_number == 0 or row_number == (height - 1):
                row_line.append("#")
            else:
                if col_number == 0 or col_number == width - 1:
                    row_line.append("#")
                else:
                    row_line.append(".")
        board.append(row_line)
    if gates_coordinates_x == 0:
        board[gates_coordinates_x][gates_coordinates_y] = GATE_SYMBOLS["up"]
    elif gates_coordinates_x == (height - 1):
        board[gates_coordinates_x][gates_coordinates_y] = GATE_SYMBOLS["down"]
    elif gates_coordinates_y == 0:
        board[gates_coordinates_x][gates_coordinates_y] = GATE_SYMBOLS["left"]
    else:
        board[gates_coordinates_x][gates_coordinates_y] = GATE_SYMBOLS["right"]
    return board


def get_gates_coordinates(col_number, row_number):

    gates_x = random.randint(0, row_number - 1)

    if gates_x == 0 or gates_x == row_number - 1:
        gates_y = random.randint(1, col_number - 2)
    else:
        gates_y = random.choice([0, col_number - 1])

    return (gates_x, gates_y)


def export_board(board, filename="level_1.txt"):
    with open(filename, "w") as f:
        for row in board:
            f.write("\t".join(row))
            f.write("\n")


def import_bord(filename="level_1.txt"):
    board = []

    with open(filename, "r") as f:
        lines = f.readlines()
    for line in lines:
        row = line.strip("\n").split("\t")
        board.append(row)

    return board


def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    if player["type"] == 'boss':
        for i in range(5):
            board[player["pos_x"] + i][player["pos_y"]] = player["icon"]
            for j in range(5):
                board[player["pos_x"] + i][player["pos_y"] + j] = player["icon"]
    else:
        board[player["pos_x"]][player["pos_y"]] = player["icon"]




def read_file(file_name):
    items_table = []
    # item_table structure by index
    # [0] = item name  [1] = type  [2] = damage  [3] = defensive  [4] = health
    text_file = open(file_name, "r")
    for line in text_file:
        items_table.append(line.strip().split("\t"))
    text_file.close()
    return items_table


def add_item_to_player(player, item, items):

    item_type_list = list(player["inventory"].keys())
    if item[ITEM_TYPE] in item_type_list:
        change_item(player, item, items)
    else:
        add_item(player, item)


def change_item(player, item, items):

    compare_items(player, item, items)
    decide = input("\n\nDo You want to change current item? Y/N  ").upper()
    while decide not in ["Y", "N"]:
        decide = input("please type 'Y' or 'N'  ").upper()
    if decide == "Y":
        remove_old_item_statistics(player, item, items)
        add_item(player, item)


def activate_cheat(player, activated):
    if not activated:
        player["maxHP"] += 2000
        player["health"] += 2000
        player["strength"] += 2000
        player["armor"] += 2000
        player["damage"] += 2000
        return 1
    else:
        player["maxHP"] -= 2000
        player["health"] -= 2000
        player["strength"] -= 2000
        player["armor"] -= 2000
        player["damage"] -= 2000
        return 0


def add_item(player, item):

    player["damage"] += int(item[ITEM_DAMAGE])
    player["armor"] += int(item[ITEM_DEFENSIVE])
    player["health"] += int(item[ITEM_HEALTH])
    player["inventory"][item[ITEM_TYPE]] = item[ITEM_NAME]


def remove_old_item_statistics(player, item, items):

    for old_item in items:
        if old_item[ITEM_NAME] == player["inventory"][item[ITEM_TYPE]]:
            player["damage"] -= int(old_item[ITEM_DAMAGE])
            player["armor"] -= int(old_item[ITEM_DEFENSIVE])
            player["health"] -= int(old_item[ITEM_HEALTH])


def compare_items(player, item, items):
    print("You already have that kind of item\n")
    details_label = ["name:", "type:", "damage:", "defense:", "health:"]
    for old_item in items:
        if old_item[ITEM_NAME] == player["inventory"][item[ITEM_TYPE]]:
            print("old item details: ")
            for i in range(len(old_item)):
                print(details_label[i], old_item[i], end="  ")
    print("\n\nnew item details:")
    for i in range(len(item)):
        print(details_label[i], item[i], end="  ")


def show_inventory(player, items):
    details_label = ["name:", "type:", "damage:", "defense:", "health:"]
    player_items_name_list = list(player["inventory"].values())
    print("Your inventory:\n")
    for item_name in player_items_name_list:
        for i in range(len(items)):
            if item_name == items[i][ITEM_NAME]:
                for j in range(len(items[i])):
                    print(details_label[j], items[i][j])
                print()


def event_handler(player: dict, board: list, level_number: list):
    if board[player["pos_x"]][player["pos_y"]] == "B":
        has_won = battlePhase.combat(player, enemy_hero)
        util.clear_screen()
        winsound.PlaySound('soun2.wav', winsound.SND_ASYNC)
        if has_won:
            board[player["pos_x"]][player["pos_y"]] = "."
            items = read_file("items.txt")
            random_item = random.randint(0, 9)
            print(items[random_item])
            add_item_to_player(player, items[random_item], items)
            enemy_hero["is_alive"] = False
        else:
            player["pos_y"] = player["pos_y"] - 5
            player["health"] = int(player["maxHP"] / 2)
            player["lives"] -= 1

    if board[player["pos_x"]][player["pos_y"]] == "M":
        has_won = battlePhase.combat(player, mercenary)
        util.clear_screen()
        # winsound.PlaySound('soun2.wav', winsound.SND_ASYNC)
        if has_won:
            board[player["pos_x"]][player["pos_y"]] = "."
            mercenary["is_alive"] = False
            items = read_file("items.txt")
            random_item = random.randint(0, 9)
            print(items[random_item])
            add_item_to_player(player, items[random_item], items)
        else:
            player["pos_y"] = player["pos_y"] - 1
            player["health"] = int(player["maxHP"] / 2)
            player["lives"] -= 1

    if board[player["pos_x"]][player["pos_y"]] == "T":
        has_won = battlePhase.combat(player, infantry_of_Troy)
        util.clear_screen()
        # winsound.PlaySound('soun2.wav', winsound.SND_ASYNC)
        if has_won:
            board[player["pos_x"]][player["pos_y"]] = "."
            infantry_of_Troy["is_alive"] = False
            items = read_file("items.txt")
            random_item = random.randint(0, 9)
            print(items[random_item])
            add_item_to_player(player, items[random_item], items)
        else:
            player["pos_y"] = player["pos_y"] - 1
            player["health"] = int(player["maxHP"] / 2)
            player["lives"] -= 1

    if board[player["pos_x"]][player["pos_y"]] == "C":
        has_won = battlePhase.combat(player, cavalry_of_Troy)
        util.clear_screen()
        # winsound.PlaySound('soun2.wav', winsound.SND_ASYNC)
        if has_won:
            board[player["pos_x"]][player["pos_y"]] = "."
            cavalry_of_Troy["is_alive"] = False
            items = read_file("items.txt")
            random_item = random.randint(0, 9)
            print(items[random_item])
            add_item_to_player(player, items[random_item], items)
        else:
            player["pos_y"] = player["pos_y"] - 1
            player["health"] = int(player["maxHP"] / 2)
            player["lives"] -= 1

    if board[player["pos_x"]][player["pos_y"]] == "I":
        print("Wbiles na I")
        items = read_file("items.txt")
        random_item = random.randint(0, 9)
        add_item_to_player(player, items[random_item], items)

    if board[player["pos_x"]][player["pos_y"]] in GATE_SYMBOLS.values():
        level_number[0] += 1
        player["pos_x"] = 3
        player["pos_y"] = 3
