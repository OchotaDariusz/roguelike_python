
import util
import engine
import ui
import player_movement
import sys
from HeroAndMonsters import cavalry_of_Troy, enemy_hero, infantry_of_Troy, mercenary
import random

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player(race: str):
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    if race.startswith("H"):
        player = {
            "name": "Player",
            "type": "player",
            "race": "human",
            "level": 1,
            "xp": 0,
            "next_level": 25,
            "lives": 3,
            "strength": 100,
            "health": 200,
            "maxHP": 200,
            "armor": 60,
            "damage": 50,
            "reward": 0,
            "pos_x": PLAYER_START_X,
            "pos_y": PLAYER_START_Y,
            "icon": PLAYER_ICON,
            "inventory": {"potion": 5}
        }
    elif race.startswith("E"):
        player = {
            "name": "Player",
            "type": "player",
            "race": "elf",
            "level": 1,
            "xp": 0,
            "next_level": 25,
            "lives": 3,
            "strength": 100,
            "health": 160,
            "maxHP": 160,
            "armor": 20,
            "damage": 80,
            "reward": 0,
            "pos_x": PLAYER_START_X,
            "pos_y": PLAYER_START_Y,
            "icon": PLAYER_ICON,
            "inventory": {"potion": 5}
        }
    elif race.startswith("D"):
        player = {
            "name": "Player",
            "type": "player",
            "race": "dwarf",
            "level": 1,
            "xp": 0,
            "next_level": 25,
            "lives": 3,
            "strength": 100,
            "health": 250,
            "maxHP": 250,
            "armor": 80,
            "damage": 30,
            "reward": 0,
            "pos_x": PLAYER_START_X,
            "pos_y": PLAYER_START_Y,
            "icon": PLAYER_ICON,
            "inventory": {"potion": 5}
        }
    return player


def main():
    cheats_active = 0

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
    level_number = [1]

    util.clear_screen()

    turn = 0

    bronze_key = 0
    silver_key = 0
    golden_key = 0

    is_running = True
    while is_running:
        turn += 1

        keys = bronze_key, silver_key, golden_key

        level_file = "level_"+str(level_number[0])+".txt"
        board = engine.import_bord(level_file)

        engine.put_player_on_board(board, player)

        if level_number[0] == 4 and enemy_hero["is_alive"]:
            engine.put_player_on_board(board, enemy_hero)

        if level_number[0] == 1 and mercenary["is_alive"]:
            engine.put_player_on_board(board, mercenary)

        if level_number[0] == 1 and not mercenary["is_alive"]:
            if bronze_key == 0:
                board[1][1] = "K"

        if level_number[0] == 2 and infantry_of_Troy["is_alive"]:
            engine.put_player_on_board(board, infantry_of_Troy)

        if level_number[0] == 2 and not infantry_of_Troy["is_alive"]:
            if silver_key == 0:
                board[1][1] = "K"

        if level_number[0] == 3 and cavalry_of_Troy["is_alive"]:
            engine.put_player_on_board(board, cavalry_of_Troy)

        if level_number[0] == 3 and not cavalry_of_Troy["is_alive"]:
            if golden_key == 0:
                board[1][1] = "K"

        ui.display_board(board)
        ui.display_stats(player)

        backup_pos_x = player["pos_x"]
        backup_pos_y = player["pos_y"]

        key = util.key_pressed()
        if key == 'q':
            is_running = False

        elif key == 'x':
            cheats_active = engine.activate_cheat(player, cheats_active)

        elif key == 'i':
            util.clear_screen()
            engine.show_inventory(player, items)
            bronze_key, silver_key, golden_key = keys
            print("Bronze Key:", bronze_key)
            print("Silver Key:", silver_key)
            print("Golden Key:", golden_key)
            keys = bronze_key, silver_key, golden_key
            util.key_pressed()

        elif key == '\\':
            util.clear_screen()
            util.save_game(player)
            print("Game Saved")
            util.key_pressed()

        else:
            player_movement.step_direction(player, key, board)

            if enemy_hero["is_alive"] and turn % 2 == 0:
                rand_key = random.choice(["W", "S", "D", "A"])
                player_movement.step_direction(enemy_hero, rand_key, board)

            if mercenary["is_alive"] and turn % 2 == 0:
                rand_key = random.choice(["W", "S", "D", "A"])
                player_movement.step_direction(mercenary, rand_key, board)

            if infantry_of_Troy["is_alive"] and turn % 2 == 0:
                rand_key = random.choice(["W", "S", "D", "A"])
                player_movement.step_direction(
                    infantry_of_Troy, rand_key, board)

            if cavalry_of_Troy["is_alive"] and turn % 2 == 0:
                rand_key = random.choice(["W", "S", "D", "A"])
                player_movement.step_direction(
                    cavalry_of_Troy, rand_key, board)

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
            sys.exit()


if __name__ == '__main__':
    main()
