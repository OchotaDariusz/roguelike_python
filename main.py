
import util
import engine
import ui
import player_movement
import sys
from HeroAndMonsters import enemy_hero
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
    # engine.add_item_to_player(player,items[1],items)
    # engine.add_item_to_player(player,items[2],items)
    # engine.add_item_to_player(player,items[3],items)
    # engine.add_item_to_player(player,items[4],items)
    # print(player)
    # engine.show_inventory(player,items)
    # input()

    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    # player = create_player()
    #SYLWEK# items = engine.read_file("items.txt")
    #SYLWEK# print(player)
    #SYLWEK# engine.add_item_to_player(player,items[2],items)
    #SYLWEK# engine.add_item_to_player(player,items[3],items)
    #SYLWEK# print(player)
    #SYLWEK# engine.add_item_to_player(player,items[7],items)
    #SYLWEK# print(player)
    #SYLWEK# print(engine.show_inventory(player))
    #SYLWEK# input()
    for level_number in range(1,4):
        level_file = "level_"+str(level_number)+".txt"
        board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
        engine.export_board(board,level_file)
    level_number = [1]

    #board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    board[5][5] = "M"
    board[7][7] = "I"

    board[9][9] = "#"
    board[10][9] = "#"
    board[11][9] = "#"
    board[12][9] = "#"
    board[13][19] = "#"
    board[14][9] = "#"
    board[9][13] = "#"
    board[9][12] = "#"
    board[9][10] = "#"
    board[9][11] = "#"
    board[9][14] = "#"
    board[9][15] = "#"

    util.clear_screen()
    is_running = True
    while is_running:
        level_file = "level_"+str(level_number[0])+".txt"
        board = engine.import_bord(level_file)
        engine.put_player_on_board(board, player)
        if enemy_hero["is_alive"]:
            engine.put_player_on_board(board, enemy_hero)
        ui.display_board(board)
        print(player)

        backup_pos_x = player["pos_x"]
        backup_pos_y = player["pos_y"]

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        elif key == 'x':
            engine.activate_cheat(player)
        elif key == 'i':
            engine.show_inventory(player, items)
            input()
        else:
            player_movement.step_direction(player, key, board)
            if enemy_hero["is_alive"]:
                rand_key = random.choice(["W", "S", "D", "A"])
                player_movement.step_direction(enemy_hero, rand_key, board)
        board[backup_pos_x][backup_pos_y] = '.'
        util.clear_screen()
        engine.event_handler(player, board, level_number)
        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] == 'B':
                    board[row][column] = '.'
        if player["lives"] <= 0:
            input("Game Over!")
            sys.exit()


if __name__ == '__main__':
    main()
