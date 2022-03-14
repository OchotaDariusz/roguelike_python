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

def read_file(file_name):
    items_table = []
    #item_table structure by index
    #[0] = item name  [1] = type  [2] = damage  [3] = defensive  [4] = health
    text_file = open(file_name , "r")
    for line in text_file:
        items_table.append(line.strip().split("\t"))
    text_file.close()
    return items_table


