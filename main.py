
import util
import engine
import ui
import player_movement

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
        "strength": 10,
        "health": 1000,
        "armor": 50,
        "damage": 30,
        "reward": 0,
        "pos_x": PLAYER_START_X,
        "pos_y": PLAYER_START_Y,
        "icon": PLAYER_ICON,
        "inventory": {}
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

    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    board[5][5] = "M"
    # board[7][7] = "I"
    # board[10][10] = "#"
    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)

        backup_pos_x = player["pos_x"]
        backup_pos_y = player["pos_y"]

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        else:
            player_movement.step_direction(player, key, board)
        board[backup_pos_x][backup_pos_y] = '.'
        util.clear_screen()
        engine.event_handler(player, board)


if __name__ == '__main__':
    main()
