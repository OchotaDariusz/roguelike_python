from board import level

def create_board(width, height):

    level_0 = level[0].split("\n")
    level_0_map = list()
    for line in level_0:
        level_0_line = [element for element in line]
        level_0_map.append(level_0_line)
    for line in level_0_map:
        # print(line)
        for element_index in range(len(line)):
            if element_index != len(line) - 1:
                print(line[element_index], end="")
            else:
                print(line[element_index])


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
