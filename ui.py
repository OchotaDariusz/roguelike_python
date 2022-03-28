from engine import GATE_SYMBOLS

COLORS_1 = {
    "border": (0, 255, 0),
    "player": (255, 255, 255),
    "item": (200, 200, 100),
    "empty space": (255, 153, 51),
    "white space": (0, 0, 0),
    "gate": (255, 255, 100),
    "M": (255, 255, 100),
    "B": (255, 255, 100),
    "I": (255, 155, 100),
    "§": (255, 255, 255),
    "K": (255, 155, 100),
    "W": (255, 155, 100),
    "C": (255, 255, 100),
    "T": (255, 255, 100)
}

COLORS_2 = {
    "border": (0, 153, 0),
    "player": (255, 255, 255),
    "item": (200, 200, 100),
    "empty space": (0, 102, 0),
    "white space": (0, 0, 0),
    "gate": (255, 255, 100),
    "M": (255, 255, 100),
    "B": (255, 255, 100),
    "I": (255, 155, 100),
    "§": (255, 255, 255),
    "W": (255, 155, 100),
    "S": (255, 155, 100),
    "C": (255, 255, 100),
    "T": (255, 255, 100)
}

COLORS_3 = {
    "border": (0, 0, 0),
    "player": (255, 255, 255),
    "item": (200, 200, 100),
    "empty space": (0, 0, 0),
    "white space": (0, 0, 0),
    "gate": (255, 255, 100),
    "M": (255, 255, 100),
    "B": (255, 255, 100),
    "I": (255, 155, 100),
    "§": (255, 255, 255),
    "K": (255, 155, 100),
    "W": (255, 155, 100),
    "C": (255, 255, 100),
    "T": (255, 255, 100)
}

COLORS_4 = {
    "border": (0, 0, 153),
    "player": (255, 255, 255),
    "item": (200, 200, 100),
    "empty space": (0, 0, 102),
    "white space": (0, 0, 0),
    "gate": (255, 255, 100),
    "M": (255, 255, 100),
    "B": (255, 255, 100),
    "I": (255, 155, 100),
    "§": (255, 255, 255),
    "K": (255, 155, 100),
    "W": (255, 155, 100),
    "C": (255, 255, 100),
    "T": (255, 255, 100)
}

SYMBOLS_DICTIONARY = {
    "I": "I",
    "§": "§",
    "K": "K",
    "M": "M",
    "W": "W",
    "B": "B",
    "T": "T",
    "C": "C",
    "#": "border",
    GATE_SYMBOLS["hell"]: "gate",
    GATE_SYMBOLS["next"]: "gate",
    GATE_SYMBOLS["previous"]: "gate",
    "@": "player",
    ".": "empty space",
    " ": "white space"
}


def get_colored(sign, level_number):
    if level_number == 1:
        color = COLORS_1[SYMBOLS_DICTIONARY[sign]]
    elif level_number == 2:
        color = COLORS_2[SYMBOLS_DICTIONARY[sign]]
    elif level_number == 3:
        color = COLORS_3[SYMBOLS_DICTIONARY[sign]]
    elif level_number == 4:
        color = COLORS_4[SYMBOLS_DICTIONARY[sign]]

    r = color[0]
    g = color[1]
    b = color[2]
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, sign)


def display_board(board: list, level_number):
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
                row += get_colored(board[i][j], level_number)
            else:
                row += get_colored(board[i][j], level_number)
        print(row)


def display_stats(player):

    print("XP: {}/{:<8} {:>9} {:>9}{} {:>18}{}".format(player["xp"], player["next_level"], player["race"],"Level: ", player["level"], "Lives: ",player["lives"], ))
    print("\n{:<23}Strength: {}".format(" ", player["strength"]))
    print("\n{:<23}Damage: {}".format(" ", player["damage"]))
    print("\n{:<23}Armor: {}".format(" ", player["armor"]))
    print("\n{:<23}HP: {}/{}".format(" ", player["health"], player["maxHP"]))
    print("\n{:<23}HP potions: {}".format(" ", player["inventory"]["potion"]))
