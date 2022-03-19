import battle
import random
import util
from monsters import cavalry_of_troy, enemy_hero, infantry_of_troy, mercenary

GATE_SYMBOLS = {
    "next": ">",
    "previous": "<",
}

ITEM_NAME = 0
ITEM_TYPE = 1
ITEM_DAMAGE = 2
ITEM_DEFENSIVE = 3
ITEM_HEALTH = 4


def create_board(width, height, level_number):
    board = []
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
    if level_number == 1:
        gate_coordinates_x, gate_coordinates_y = int(height/2), width - 1
        board[gate_coordinates_x][gate_coordinates_y] = GATE_SYMBOLS["next"]
    elif level_number == 4:
        back_gate_coordinates_x, back_gate_coordinates_y = int(height/2), 0
        board[back_gate_coordinates_x][back_gate_coordinates_y] = GATE_SYMBOLS["previous"]
    else:
        gate_coordinates_x, gate_coordinates_y = int(height/2), width - 1
        back_gate_coordinates_x, back_gate_coordinates_y = int(height/2), 0
        board[gate_coordinates_x][gate_coordinates_y] = GATE_SYMBOLS["next"]
        board[back_gate_coordinates_x][back_gate_coordinates_y] = GATE_SYMBOLS["previous"]
    return board


"""def get_gates_coordinates(col_number, row_number):

    gates_x = random.randint(0, row_number - 1)

    if gates_x == 0 or gates_x == row_number - 1:
        gates_y = random.randint(1, col_number - 2)
    else:
        gates_y = random.choice([0, col_number - 1])

    return (gates_x, gates_y)
"""


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
    text_file = open(file_name, "r")
    for line in text_file:
        items_table.append(line.strip().split("\t"))
    text_file.close()
    return items_table


def remove_old_item_statistics(player, item, items):
    for old_item in items:
        if old_item[ITEM_NAME] == player["inventory"][item[ITEM_TYPE]]:
            player["damage"] -= int(old_item[ITEM_DAMAGE])
            player["armor"] -= int(old_item[ITEM_DEFENSIVE])
            player["health"] -= int(old_item[ITEM_HEALTH])
            player["maxHP"] -= int(old_item[ITEM_HEALTH])


def add_item(player, item):
    player["damage"] += int(item[ITEM_DAMAGE])
    player["armor"] += int(item[ITEM_DEFENSIVE])
    player["health"] += int(item[ITEM_HEALTH])
    player["maxHP"] += int(item[ITEM_HEALTH])
    player["inventory"][item[ITEM_TYPE]] = item[ITEM_NAME]


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


def change_item(player, item, items):
    compare_items(player, item, items)
    decide = input("\n\nDo You want to change current item? Y/N  ").upper()
    while decide not in ["Y", "N"]:
        decide = input("please type 'Y' or 'N'  ").upper()
    if decide == "Y":
        remove_old_item_statistics(player, item, items)
        add_item(player, item)


def add_item_to_player(player, item, items):
    item_type_list = list(player["inventory"].keys())
    if item[ITEM_TYPE] in item_type_list:
        change_item(player, item, items)
    else:
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
    print("Health Potions:", player["inventory"]["potion"])


def event_handler_monsters(player, board, enemy, items):
    has_won = battle.combat(player, enemy)
    util.clear_screen()
    if has_won is True:
        board[player["pos_x"]][player["pos_y"]] = "."
        enemy["is_alive"] = False
        random_item = random.randint(0, 9)
        print(items[random_item])
        add_item_to_player(player, items[random_item], items)
    else:
        enemy_size = 1 if enemy["type"] == "monster" else 5
        player["pos_y"] = player["pos_y"] - enemy_size
        player["health"] = int(player["maxHP"] / 2)
        player["lives"] -= 1


def pick_up_key(player, board, level_number, level, key):
    if board[player["pos_x"]][player["pos_y"]] == "K" and \
       level_number == level:
        print("You have found a key!")
        key += 1
        board[player["pos_x"]][player["pos_y"]] == "."
    return key


def check_if_monster(player, board, enemy, items):
    if board[player["pos_x"]][player["pos_y"]] == enemy["icon"]:
        event_handler_monsters(player, board, enemy, items)


def check_for_keys(player, board, level_number, keys):
    bronze_key, silver_key, golden_key = keys
    bronze_key = pick_up_key(player, board, level_number, 1, bronze_key)
    silver_key = pick_up_key(player, board, level_number, 2, silver_key)
    golden_key = pick_up_key(player, board, level_number, 3, golden_key)
    return bronze_key, silver_key, golden_key


def check_for_monsters(player, board, items):
    monsters = [mercenary, infantry_of_troy, cavalry_of_troy, enemy_hero]
    for monster in monsters:
        check_if_monster(player, board, monster, items)


def check_for_items(player, board, items):
    if board[player["pos_x"]][player["pos_y"]] == "I":
        random_item = random.randint(0, 9)
        add_item_to_player(player, items[random_item], items)


def check_floor(player, board, level_number, keys, items):
    check_for_monsters(player, board, items)
    check_for_items(player, board, items)
    return check_for_keys(player, board, level_number, keys)


def previous_level(player, level_number):
    level_number -= 1
    player["pos_x"] = 10
    player["pos_y"] = 28
    return level_number


def next_level(player, level_number):
    level_number += 1
    player["pos_x"] = 10
    player["pos_y"] = 1
    return level_number


def check_for_gate(player, board, level_number, keys):
    bronze_key, silver_key, golden_key = keys
    if board[player["pos_x"]][player["pos_y"]] in GATE_SYMBOLS["next"]:
        if level_number == 1 and bronze_key == 1:
            level_number = next_level(player, level_number)
        elif level_number == 2 and silver_key == 1:
            level_number = next_level(player, level_number)
        elif level_number == 3 and golden_key == 1:
            level_number = next_level(player, level_number)
        else:
            print("You need a key!")
            player["pos_x"] = 10
            player["pos_y"] = 28
    elif board[player["pos_x"]][player["pos_y"]] in GATE_SYMBOLS["previous"]:
        level_number = previous_level(player, level_number)
    return level_number


def event_handler(player: dict, board: list, level_number: int, keys, items):
    bronze_key, silver_key, golden_key = check_floor(
        player, board, level_number, keys, items)
    keys = bronze_key, silver_key, golden_key
    level_number = check_for_gate(player, board, level_number, keys)
    return level_number, keys
