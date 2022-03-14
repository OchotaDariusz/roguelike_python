import random

GATE_SYMBOLS = {
"up": "\u25B2",
"down": "\u25BC",
"left": "\u25C4",
"right": "\u25BA"
}

def create_board(width, height):
    board = []
    gates_coordinates_x, gates_coordinates_y = get_gates_coordinates(width, height)
    for row_number in range(height):
        row_line = []
        for col_number in range(width):
            if row_number == 0 or row_number == (height-1):
                row_line.append("#")
            else: 
                if col_number == 0 or col_number == width-1: 
                    row_line.append("#")
                else:
                    row_line.append(".")
        board.append(row_line)
    if gates_coordinates_x == 0:
        board[gates_coordinates_x][gates_coordinates_y] = GATE_SYMBOLS["up"]
    elif gates_coordinates_x == (height - 1):
        board[gates_coordinates_x][gates_coordinates_y] = GATE_SYMBOLS["down"]
    elif gates_coordinates_y == 0:
        board[gates_coordinates_x][gates_coordinates_y] = GATE_SYMBOLS["left"]
    else:
        board[gates_coordinates_x][gates_coordinates_y] = GATE_SYMBOLS["right"]
    return board


def get_gates_coordinates(col_number,row_number):

    gates_x = random.randint(0, row_number-1)

    if gates_x == 0 or gates_x == row_number-1:
        gates_y = random.randint(1, col_number-2)
    else:
        gates_y = random.choice([0, col_number-1])

    return (gates_x,gates_y)


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
