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
    "K": (255, 155, 100),
    "C": (255, 255, 100),
    "T": (255, 255, 100)
}

SYMBOLS_DICTIONARY = {
    "I": "I",
    "K": "K",
    "M": "M",
    "B": "B",
    "T": "T",
    "C": "C",
    "#": "border",
    GATE_SYMBOLS["next"]: "gate",
    GATE_SYMBOLS["previous"]: "gate",
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


def display_stats(player):

    print("XP: {}/{:<8} {:>9} {:>9}{} {:>18}{}".format(player["xp"], player["next_level"], player["race"],"Level: ", player["level"], "Lives: ",player["lives"], ))
    print("\n{:<23}Strength: {}".format(" ", player["strength"]))
    print("\n{:<23}Damage: {}".format(" ", player["damage"]))
    print("\n{:<23}Armor: {}".format(" ", player["armor"]))
    print("\n{:<23}HP: {}/{}".format(" ", player["health"], player["maxHP"]))
    print("\n{:<23}HP potions: {}".format(" ", player["inventory"]["potion"]))
