def create_board(width, height):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    pass


def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    pass

ITEM_NAME = 0
ITEM_TYPE = 1
ITEM_DAMAGE = 2
ITEM_DEFENSIVE = 3
ITEM_HEALTH = 4

def read_file(file_name):
    items_table = []
    #item_table structure by index
    #[0] = item name  [1] = type  [2] = damage  [3] = defensive  [4] = health
    text_file = open(file_name , "r")
    for line in text_file:
        items_table.append(line.strip().split("\t"))
    text_file.close()
    return items_table

def add_item_to_player(player,item):
    if item[ITEM_DAMAGE] != 0 :
        player["damage"] += int(item[ITEM_DAMAGE])
    if item[ITEM_DEFENSIVE] != 0 :
        player["armor"] += int(item[ITEM_DEFENSIVE])    
    if item[ITEM_HEALTH] != 0 :
        player["health"] += int(item[ITEM_HEALTH])
    player["inventory"].append(item[ITEM_NAME])