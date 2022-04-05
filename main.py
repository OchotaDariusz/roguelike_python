import os
from data import ascii_art
from data import engine
from data import ui
from data import util

PLAYER_ICON = '@'
PLAYER_START_X = 13
PLAYER_START_Y = 13
LOGO_COLOR = '\033[93m'
COLOR_RESET = '\033[0m'
BOARD_WIDTH = 40
BOARD_HEIGHT = 30


def display_opening():
    engine.slow_print(
        "Once upon a time, there was a fortunate land called Codecool. ")
    engine.slow_print("In this land lived happily a man named Student.")
    print("\n\n")
    engine.slow_print(
        "He lived in peace and prosperity, learning the Programming Basics - Python module, ")
    print()
    engine.slow_print(
        "until one day the wraith of the final exam came to the land.")
    print()
    engine.slow_print("Suddenly everyone became unhappy and stressed out.")
    print("\n\n")
    engine.slow_print("The atmosphere of terror grew at an alarming rate.")
    print()
    engine.slow_print("The amount of energy drinks drunk, ")
    engine.slow_print(
        "cigarettes smoked and alcohol consumed went over scale!")
    print("\n\n")
    engine.slow_print(
        "Our Student was chosen to face this pure evil and restore peace to the land, ")
    engine.slow_print(
        "he must abandon his current life and set off on a dangerous journey to finally deal with the final exam...")
    input("\n\nPress ENTER to continue...")
    util.clear_screen()


def display_instruction():
    engine.slow_print("Instructions:")
    print("\n\n")
    engine.slow_print("Press W,A,S,D to move")
    print()
    engine.slow_print("Press I to show inventory")
    print()
    engine.slow_print("Press P to show player statistics")
    print()
    engine.slow_print("Press \\ to save the game")
    print()
    engine.slow_print("Press X to activate cheats")
    print()
    engine.slow_print("Press Q to quit")
    input("\n\nPress ENTER to continue...")
    util.clear_screen()


def intro():
    print(LOGO_COLOR + ascii_art.logo + COLOR_RESET)
    print("Press any key to Play")
    util.key_pressed()
    util.clear_screen()
    display_opening()
    display_instruction()


def choose_race(race, player):
    if race.startswith("E"):
        player["race"] = "elf"
        player["strength"] = 80
        player["health"] = 160
        player["max_hp"] = player["health"]
        player["armor"] = 20
        player["damage"] = 80
        player["mana"] = 86
        player["max_mana"] = 86
    elif race.startswith("D"):
        player["race"] = "dwarf"
        player["strength"] = 120
        player["health"] = 200
        player["max_hp"] = player["health"]
        player["armor"] = 80
        player["damage"] = 30
        player["mana"] = 86
        player["max_mana"] = 86
    else:
        player["race"] = "human"
        player["strength"] = 100
        player["health"] = 200
        player["max_hp"] = player["health"]
        player["armor"] = 60
        player["damage"] = 50
        player["mana"] = 87
        player["max_mana"] = 87


def create_player(race: str):
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player = {
        "name": "Player",
        "type": "player",
        "race": None,
        "level": 1,
        "xp": 0,
        "next_level": 25,
        "lives": 3,
        "strength": 100,
        "health": None,
        "max_hp": None,
        "mana": None,
        "max_mana": None,
        "armor": None,
        "damage": None,
        "reward": 0,
        "pos_x": PLAYER_START_X,
        "pos_y": PLAYER_START_Y,
        "icon": PLAYER_ICON,
        "inventory": {"health_potion": 5,
                      "mana_potion": 2}
    }

    choose_race(race, player)
    return player


def new_player():
    race = input("Choose your race(Human, Elf, Dwarf): ").upper()
    player = create_player(race)
    return player


def load_player():
    player = util.load_game()
    player["pos_x"] = PLAYER_START_X
    player["pos_y"] = PLAYER_START_Y
    player["icon"] = PLAYER_ICON
    return player


def setup_player():
    start_game = input("1) Start New Game\n2) Load Last Game\n")
    if start_game == '2':
        player = load_player()
    else:
        player = new_player()
    return player


def setup_items():
    items = engine.read_file(os.path.dirname(
        os.path.abspath(__file__)) + "/data/items/items.txt")
    return items


def generate_levels():
    for level_number in range(1, 5):
        level_file = os.path.dirname(os.path.abspath(
            __file__)) + "/data/levels/level_" + str(level_number) + ".txt"
        board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT, level_number)
        engine.export_board(board, level_file)


def setup_game():
    screen_size = 10
    player, items = setup_player(), setup_items()
    level_number, cheats_active, turn = 1, 0, 0
    size = BOARD_HEIGHT, BOARD_WIDTH
    milestones = 0, 0, 0
    exam_permission = 0
    generate_levels()
    return turn, player, items, level_number, screen_size, cheats_active, size, exam_permission, milestones


def setup_map(player, level_number, size, milestones):
    level_file = os.path.dirname(os.path.abspath(
        __file__)) + "/data/levels/level_" + str(level_number) + ".txt"
    board = engine.import_bord(level_file)
    engine.initialize_map(player, level_number, board, size, milestones)
    return board


def display_ui(screen_size, player, level_number, board):
    ui.display(board, player["pos_y"], player["pos_x"],
               screen_size, level_number)
    ui.display_stats(player)


def main():
    util.clear_screen()
    intro()
    turn, player, items, level_number, screen_size, cheats_active, size, exam_pass, milestones = setup_game()
    util.play_sound("opening")
    is_game_running = True
    util.clear_screen()
    while is_game_running:
        turn += 1
        board = setup_map(player, level_number, size, milestones)
        display_ui(screen_size, player, level_number, board)
        backup_pos_x = player["pos_x"]
        backup_pos_y = player["pos_y"]
        key = util.key_pressed()
        is_game_running, cheats_active = engine.key_handler(
            player, items, cheats_active,
            turn, milestones, board,
            key, level_number, exam_pass)
        if is_game_running is False:
            break
        util.clear_screen()
        level_number, milestones, exam_pass, is_game_running = engine.event_handler(
            player, board, level_number,
            milestones, items, exam_pass)
        board[backup_pos_x][backup_pos_y] = '.'
        if player["lives"] <= 0:
            input("Game Over!")
            is_game_running = False


if __name__ == '__main__':
    main()
