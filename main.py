
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


player = {
    "name": "Player",
    "health": 1000,
    "armor": 50,
    "damage": 10,
    "pos_x": PLAYER_START_X,
    "pos_y": PLAYER_START_Y,
    "icon": PLAYER_ICON,
    "inventory": {}
}


def main():
    cheats_active = 0
    race = input("Choose your race(Human, Elf, Dwarf): ")
    player = create_player(race)
    # SYLWEK# items = engine.read_file("items.txt")
    # SYLWEK# print(player)
    # SYLWEK# engine.add_item_to_player(player,items[2],items)
    # SYLWEK# engine.add_item_to_player(player,items[3],items)
    # SYLWEK# print(player)
    # SYLWEK# engine.add_item_to_player(player,items[7],items)
    # SYLWEK# print(player)
    # SYLWEK# print(engine.show_inventory(player))
    # SYLWEK# input()
    items = engine.read_file("items.txt")
    # print(player)
    #engine.add_item_to_player(player,items[1],items)
    #engine.add_item_to_player(player,items[2],items)
    #engine.add_item_to_player(player,items[8],items)
    #engine.add_item_to_player(player,items[9],items)
    # print(player)
    # engine.show_inventory(player,items)
    # input()

    # board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    # player = create_player()
    # SYLWEK# items = engine.read_file("items.txt")
    # SYLWEK# print(player)
    # SYLWEK# engine.add_item_to_player(player,items[2],items)
    # SYLWEK# engine.add_item_to_player(player,items[3],items)
    # SYLWEK# print(player)
    # SYLWEK# engine.add_item_to_player(player,items[7],items)
    # SYLWEK# print(player)
    # SYLWEK# print(engine.show_inventory(player))
    # SYLWEK# input()
    for level_number in range(1, 5):
        level_file = "level_"+str(level_number)+".txt"
        board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
        engine.export_board(board, level_file)
    level_number = [1]

    #board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    board[5][5] = "M"  # to delete
    board[7][7] = "I"  # to delete

    board[9][9] = "#"  # to delete
    board[10][9] = "#"  # to delete
    board[11][9] = "#"  # to delete
    board[12][9] = "#"  # to delete
    board[13][19] = "#"  # to delete
    board[14][9] = "#"  # to delete
    board[9][13] = "#"  # to delete
    board[9][12] = "#"  # to delete
    board[9][10] = "#"  # to delete
    board[9][11] = "#"  # to delete
    board[9][14] = "#"  # to delete
    board[9][15] = "#"  # to delete

    util.clear_screen()

    turn = 0

    is_running = True
    while is_running:
        turn += 1

        level_file = "level_"+str(level_number[0])+".txt"
        board = engine.import_bord(level_file)

        engine.put_player_on_board(board, player)

        if level_number[0] == 4 and enemy_hero["is_alive"]:
            engine.put_player_on_board(board, enemy_hero)

        if level_number[0] == 1 and mercenary["is_alive"]:
            engine.put_player_on_board(board, mercenary)

        if level_number[0] == 2 and infantry_of_Troy["is_alive"]:
            engine.put_player_on_board(board, infantry_of_Troy)

        if level_number[0] == 3 and cavalry_of_Troy["is_alive"]:
            engine.put_player_on_board(board, cavalry_of_Troy)
        ui.display_board(board)
        engine.display_stats(player)

        backup_pos_x = player["pos_x"]
        backup_pos_y = player["pos_y"]

        key = util.key_pressed()
        if key == 'q':
            is_running = False

        elif key == 'x':
            cheats_active = engine.activate_cheat(player, cheats_active)

        elif key == 'i':
            engine.show_inventory(player, items)
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

        engine.event_handler(player, board, level_number)

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
