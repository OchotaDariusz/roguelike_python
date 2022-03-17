import sys
import os


def key_pressed():
    try:
        import tty
        import termios
    except ImportError:
        try:
            # probably Windows
            import msvcrt
        except ImportError:
            # FIXME what to do on other platforms?
            raise ImportError('getch not available')
        else:
            key = msvcrt.getch().decode('utf-8')
            return key
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def save_game(player):
    backup_inv = dict()
    player_save = ""
    for k, v in player.items():
        player_save += k
        player_save += ";"
        if isinstance(v, dict):
            backup_inv = v
        else:
            player_save += str(v)
        player_save += "\n"
    save_player = open("player_save.txt", "w")
    save_player.write(player_save)
    save_player.close()

    items_save = ''
    for k, v in backup_inv.items():
        items_save += k
        items_save += ";"
        items_save += str(v)
        items_save += "\n"
    save_items = open("items_save.txt", "w")
    save_items.write(items_save)
    save_items.close()


def load_game():
    open_player_items = open("items_save.txt", "r")
    read_player_items = open_player_items.readlines()
    key_value = [element.strip("\n").split(';') for element in read_player_items]
    open_player_items.close()

    item_dict = dict()
    for i in range(len(key_value)):
        if key_value[i][1].isdigit():
            item_dict[key_value[i][0]] = int(key_value[i][1])
        elif key_value[i][1] == "":
            player_dict[key_value[i][0]] = key_value[i][1]
        else:
            item_dict[key_value[i][0]] = key_value[i][1]

    open_player_save = open("player_save.txt", "r")
    read_player_save = open_player_save.readlines()
    key_value = [element.strip("\n").split(';') for element in read_player_save]
    open_player_save.close()

    player_dict = dict()
    for i in range(len(key_value)):
        if key_value[i][1].isdigit():
            player_dict[key_value[i][0]] = int(key_value[i][1])
        elif key_value[i][1] == "":
            player_dict[key_value[i][0]] = item_dict
        else:
            player_dict[key_value[i][0]] = key_value[i][1]

    return player_dict
