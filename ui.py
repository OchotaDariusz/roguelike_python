from engine import GATE_SYMBOLS

COLORS = {
    "border": (200, 100, 10),
    "player": (255, 255, 255),
    "item": (200, 200, 100),
    "empty space": (102, 255, 102),
    "gate": (255, 255, 100),
    "M": (255, 255, 100),
    "B": (255, 255, 100),
    "I": (255, 155, 100),
    "C": (155, 255, 100),
    "T": (155, 155, 100)
}

SYMBOLS_DICTIONARY = {
    "I": "I",
    "M": "M",
    "B": "B",
    "T": "T",
    "C": "C",
    "#": "border",
    GATE_SYMBOLS["down"]: "gate",
    GATE_SYMBOLS["up"]: "gate",
    GATE_SYMBOLS["left"]: "gate",
    GATE_SYMBOLS["right"]: "gate",
    "@": "player",
    ".": "empty space"
}


def get_colored(sign):
    color = COLORS[SYMBOLS_DICTIONARY[sign]]

    r = color[0]
    g = color[1]
    b = color[2]
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, sign)


def display_board(board: list):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''

    print("\n")

    for i in range(len(board)):
        row = ""
        for j in range(len(board[i])):
            if j != len(board[i]) - 1:
                row += get_colored(board[i][j])
            else:
                row += get_colored(board[i][j])
        print(row)
