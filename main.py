import util
import engine
import ui
import player_movement
import sys

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player = {
        "name": "Player",
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
    return player


def main():
    player = create_player()
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
    # board[10][10] = "#"
    util.clear_screen()
    is_running = True
    while is_running:
        level_file = "level_"+str(level_number[0])+".txt"
        board = engine.import_bord(level_file)
        engine.put_player_on_board(board, player)
        ui.display_board(board)
        print(player)

        backup_pos_x = player["pos_x"]
        backup_pos_y = player["pos_y"]

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        else:
            player_movement.step_direction(player, key, board)
        board[backup_pos_x][backup_pos_y] = '.'
        util.clear_screen()
        engine.event_handler(player, board,level_number)
        if player["lives"] <= 0:
            input("Game Over!")
            sys.exit()

if __name__ == '__main__':
    main()
