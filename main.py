from data import engine
import data.ui as ui
import data.util as util


PLAYER_ICON = '@'
PLAYER_START_X = 13
PLAYER_START_Y = 13

BOARD_WIDTH = 40
BOARD_HEIGHT = 30


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
    items = engine.read_file("data/items/items.txt")
    for level_number in range(1, 5):
        level_file = "data/levels/level_"+str(level_number)+".txt"
        board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT, level_number)
        engine.export_board(board, level_file)
    return player, items


def main():
    screen_size = 10
    util.clear_screen()
    player, items = setup_game()
    level_number = 1
    cheats_active = 0
    turn = 0
    bronze_milestone, silver_milestone, golden_milestone = 0, 0, 0
    exam_permission = 0
    size = BOARD_HEIGHT, BOARD_WIDTH
    is_running = True
    util.clear_screen()
    while is_running:
        turn += 1
        milestones = bronze_milestone, silver_milestone, golden_milestone
        level_file = "data/levels/level_"+str(level_number)+".txt"
        board = engine.import_bord(level_file)
        engine.initialize_map(player, level_number, board, size, milestones)
        ui.display(board, player["pos_y"], player["pos_x"], screen_size, level_number)
        ui.display_stats(player)
        backup_pos_x = player["pos_x"]
        backup_pos_y = player["pos_y"]
        key = util.key_pressed()
        is_running, cheats_active = engine.key_handler(
            player, items, cheats_active, turn, milestones, board, key, level_number, exam_permission)
        util.clear_screen()
        level_number, milestones, exam_permission = engine.event_handler(
            player, board, level_number, milestones, items, exam_permission)
        bronze_milestone, silver_milestone, golden_milestone = milestones
        board[backup_pos_x][backup_pos_y] = '.'

        if player["lives"] <= 0:
            input("Game Over!")
            is_running = False


if __name__ == '__main__':
    main()
