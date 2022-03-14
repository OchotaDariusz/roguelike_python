
import util
import engine
import ui

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
    pass

player = {
    "name": "Player",
    "health": 1000,
    "armor": 50,
    "damage": 10,
    "pos_x": PLAYER_START_X,
    "pos_y": PLAYER_START_Y,
    "icon": PLAYER_ICON,
    "inventory":{}
}

def main():
    #player = create_player()
    items = engine.read_file("items.txt")
    print(player)
    engine.add_item_to_player(player,items[2],items)
    print(player)
    engine.add_item_to_player(player,items[7],items)
    print(player)
    input()
    
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)

    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        else:
            pass
        util.clear_screen()


if __name__ == '__main__':
    main()
