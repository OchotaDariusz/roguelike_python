import util
import engine
import ui
import movement
import sys
from monsters import cavalry_of_troy, enemy_hero, infantry_of_troy, mercenary
import random

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def choose_race(race, player):
    if race.startswith("H"):
        player["race"] = "human"
        player["strength"] = 100
        player["health"] = 200
        player["maxHP"] = player["health"]
        player["armor"] = 60
        player["damage"] = 50
    elif race.startswith("E"):
        player["race"] = "elf"
        player["strength"] = 80
        player["health"] = 160
        player["maxHP"] = player["health"]
        player["armor"] = 20
        player["damage"] = 80
    elif race.startswith("D"):
        player["race"] = "dwarf"
        player["strength"] = 120
        player["health"] = 200
        player["maxHP"] = player["health"]
        player["armor"] = 80
        player["damage"] = 30


def create_player(race: str):
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player = {
        "name": "Player",
        "type": "player",
        "race": None,
        "level": 1,
        "xp": 0,
        "next_level": 25,
        "lives": 3,
        "strength": 100,
        "health": None,
        "maxHP": None,
        "armor": None,
        "damage": None,
        "reward": 0,
        "pos_x": PLAYER_START_X,
        "pos_y": PLAYER_START_Y,
        "icon": PLAYER_ICON,
        "inventory": {"potion": 5}
    }

    choose_race(race, player)
    return player


def monster_step(board, turn, enemy):
    if enemy["is_alive"] and turn % 2 == 0:
        rand_key = random.choice(["W", "S", "D", "A"])
        movement.step_direction(enemy, rand_key, board)


def place_monster(level_number, level, board, enemy):
    if level_number[0] == level and enemy["is_alive"]:
        engine.put_player_on_board(board, enemy)


def place_key(board, level_number, level, enemy, key):
    if level_number[0] == level and not enemy["is_alive"]:
        if key == 0:
            board[1][1] = "K"


def place_monsters(level_number, board):
    monsters = [mercenary, infantry_of_troy, cavalry_of_troy, enemy_hero]
    for level, monster in enumerate(monsters):
        place_monster(level_number, level + 1, board, monster)


def move_monsters(board, turn):
    monsters = [mercenary, infantry_of_troy, cavalry_of_troy, enemy_hero]
    for monster in monsters:
        monster_step(board, turn, monster)


def initialize_map(player, level_number, board, keys):
    bronze_key, silver_key, golden_key = keys
    engine.put_player_on_board(board, player)
    place_monsters(level_number, board)
    place_key(board, level_number, 1, mercenary, bronze_key)
    place_key(board, level_number, 2, infantry_of_troy, silver_key)
    place_key(board, level_number, 3, cavalry_of_troy, golden_key)


def setup_game():
    start_game = input("1) Start New Game\n2) Load Last Game\n")
    if start_game == '1':
        race = input("Choose your race(Human, Elf, Dwarf): ").upper()
        player = create_player(race)
    else:
        player = util.load_game()
        player["pos_x"] = PLAYER_START_X
        player["pos_y"] = PLAYER_START_Y
        player["icon"] = PLAYER_ICON
    items = engine.read_file("items.txt")
    for level_number in range(1, 5):
        level_file = "level_"+str(level_number)+".txt"
        board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT, level_number)
        engine.export_board(board, level_file)
    return player, items


def key_handler(player, items, cheats_active, turn, keys, board, key):
    if key == 'q':
        return False
    elif key == 'x':
        cheats_active = engine.activate_cheat(player, cheats_active)
        return True
    elif key == 'i':
        util.clear_screen()
        engine.show_inventory(player, items)
        bronze_key, silver_key, golden_key = keys
        print("Bronze Key:", bronze_key)
        print("Silver Key:", silver_key)
        print("Golden Key:", golden_key)
        util.key_pressed()
        return True
    elif key == '\\':
        util.clear_screen()
        util.save_game(player)
        print("Game Saved")
        util.key_pressed()
        return True
    else:
        movement.step_direction(player, key, board)
        move_monsters(board, turn)
        return True


def main():
    player, items = setup_game()
    level_number = [1]
    util.clear_screen()
    cheats_active = 0
    turn = 0
    bronze_key, silver_key, golden_key = 0, 0, 0
    is_running = True
    while is_running:
        turn += 1
        keys = bronze_key, silver_key, golden_key
        level_file = "level_"+str(level_number[0])+".txt"
        board = engine.import_bord(level_file)
        initialize_map(player, level_number, board, keys)
        ui.display_board(board)
        ui.display_stats(player)
        backup_pos_x = player["pos_x"]
        backup_pos_y = player["pos_y"]
        key = util.key_pressed()
        is_running = key_handler(
            player, items, cheats_active, turn, keys, board, key)
        util.clear_screen()
        keys = engine.event_handler(player, board, level_number, keys)
        bronze_key, silver_key, golden_key = keys
        board[backup_pos_x][backup_pos_y] = '.'
        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] == 'B':
                    board[row][column] = '.'

        if player["lives"] <= 0:
            input("Game Over!")
            is_running = False


if __name__ == '__main__':
    main()
