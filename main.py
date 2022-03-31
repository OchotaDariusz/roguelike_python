import os
import winsound
from data import engine
from data import ui
from data import util

PLAYER_ICON = '@'
PLAYER_START_X = 13
PLAYER_START_Y = 13

BOARD_WIDTH = 40
BOARD_HEIGHT = 30


def display_opening():
    engine.slow_print("OPENING TEXT")
    print("\n\nPress any key to continue...")
    util.key_pressed()
    util.clear_screen()


def display_instruction():
    engine.slow_print("INSTRUCTION")
    print("\n\nPress any key to continue...")
    util.key_pressed()
    util.clear_screen()


def intro():
    display_opening()
    display_instruction()


def choose_race(race, player):
    if race.startswith("H"):
        player["race"] = "human"
        player["strength"] = 100
        player["health"] = 200
        player["maxHP"] = player["health"]
        player["armor"] = 60
        player["damage"] = 50
        player["mana"] = 100
        player["maxMana"] = 100
    elif race.startswith("E"):
        player["race"] = "elf"
        player["strength"] = 80
        player["health"] = 160
        player["maxHP"] = player["health"]
        player["armor"] = 20
        player["damage"] = 80
        player["mana"] = 100
        player["maxMana"] = 100
    elif race.startswith("D"):
        player["race"] = "dwarf"
        player["strength"] = 120
        player["health"] = 200
        player["maxHP"] = player["health"]
        player["armor"] = 80
        player["damage"] = 30
        player["mana"] = 100
        player["maxMana"] = 100


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
        "maxHP": None,
        "mana": None,
        "maxMana": None,
        "armor": None,
        "damage": None,
        "reward": 0,
        "pos_x": PLAYER_START_X,
        "pos_y": PLAYER_START_Y,
        "icon": PLAYER_ICON,
        "inventory": {"potion": 5}
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
    if start_game == '1':
        player = new_player()
    else:
        player = load_player()
    return player


def setup_items():
    items = engine.read_file(os.path.dirname(
        os.path.abspath(__file__)) + "/data/items/items.txt")
    return items


def generate_levels():
    for level_number in range(1, 5):
        level_file = os.path.dirname(os.path.abspath(
            __file__)) + "/data/levels/level_"+str(level_number)+".txt"
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
    return turn, player, items, \
        level_number, screen_size, cheats_active, \
        size, exam_permission, milestones


def setup_map(player, level_number, size, milestones):
    level_file = os.path.dirname(os.path.abspath(
        __file__)) + "/data/levels/level_"+str(level_number)+".txt"
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
    turn, player, items, \
        level_number, screen_size, cheats_active, \
        size, exam_permission, milestones = setup_game()
    winsound.PlaySound(os.path.dirname(os.path.abspath(
        __file__)) + '/data/sounds/openning.wav', winsound.SND_ASYNC)
    is_running = True
    util.clear_screen()
    while is_running:
        turn += 1
        board = setup_map(player, level_number, size, milestones)
        display_ui(screen_size, player, level_number, board)
        backup_pos_x = player["pos_x"]
        backup_pos_y = player["pos_y"]
        key = util.key_pressed()
        is_running, cheats_active = engine.key_handler(
            player, items, cheats_active,
            turn, milestones, board,
            key, level_number, exam_permission)
        if is_running is False:
            break
        util.clear_screen()
        level_number, milestones, exam_permission, is_running = engine.event_handler(
            player, board, level_number,
            milestones, items, exam_permission)
        board[backup_pos_x][backup_pos_y] = '.'
        if player["lives"] <= 0:
            input("Game Over!")
            is_running = False


if __name__ == '__main__':
    main()
