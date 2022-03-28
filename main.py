import engine
import ui
import util


PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def choose_race(race, player):
    if race.startswith("H"):
        player["race"] = "human"
        player["strength"] = 100
        player["health"] = 200
        player["maxHP"] = player["health"]
        player["armor"] = 60
        player["damage"] = 50
    elif race.startswith("E"):
        player["race"] = "elf"
        player["strength"] = 80
        player["health"] = 160
        player["maxHP"] = player["health"]
        player["armor"] = 20
        player["damage"] = 80
    elif race.startswith("D"):
        player["race"] = "dwarf"
        player["strength"] = 120
        player["health"] = 200
        player["maxHP"] = player["health"]
        player["armor"] = 80
        player["damage"] = 30


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


def setup_game():
    start_game = input("1) Start New Game\n2) Load Last Game\n")
    if start_game == '1':
        race = input("Choose your race(Human, Elf, Dwarf): ").upper()
        player = create_player(race)
    else:
        player = util.load_game()
        player["pos_x"] = PLAYER_START_X
        player["pos_y"] = PLAYER_START_Y
        player["icon"] = PLAYER_ICON
    items = engine.read_file("items.txt")
    for level_number in range(1, 5):
        level_file = "level_"+str(level_number)+".txt"
        board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT, level_number)
        engine.export_board(board, level_file)
    return player, items


def main():
    util.clear_screen()
    player, items = setup_game()
    level_number = 1
    cheats_active = 0
    turn = 0
    bronze_key, silver_key, golden_key = 0, 0, 0
    power_ring = 0
    size = BOARD_HEIGHT, BOARD_WIDTH
    is_running = True
    util.clear_screen()
    while is_running:
        turn += 1
        keys = bronze_key, silver_key, golden_key
        level_file = "level_"+str(level_number)+".txt"
        board = engine.import_bord(level_file)
        engine.initialize_map(player, level_number, board, size, keys)
        ui.display_board(board)
        ui.display_stats(player)
        backup_pos_x = player["pos_x"]
        backup_pos_y = player["pos_y"]
        key = util.key_pressed()
        is_running, cheats_active = engine.key_handler(
            player, items, cheats_active, turn, keys, board, key, level_number, power_ring)
        util.clear_screen()
        level_number, keys, power_ring = engine.event_handler(
            player, board, level_number, keys, items, power_ring)
        bronze_key, silver_key, golden_key = keys
        board[backup_pos_x][backup_pos_y] = '.'

        if player["lives"] <= 0:
            input("Game Over!")
            is_running = False


if __name__ == '__main__':
    main()
