import os
import sys
import winsound


def key_pressed():
    try:
        import tty
        import termios
    except ImportError:
        try:
            # probably Windows
            import msvcrt
        except ImportError:
            import getch
            key = getch.getch().decode('utf-8')
            return key
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


def save_player(player):
    inventory = dict()
    player_save = ""
    for k, v in player.items():
        player_save += k + ";"
        if isinstance(v, dict):
            inventory = v
        else:
            player_save += str(v)
        player_save += "\n"
    save = open("data/save/player_save.txt", "w")
    save.write(player_save)
    save.close()
    return inventory


def save_inventory(inventory):
    items = ''
    for k, v in inventory.items():
        items += k + ";" + str(v) + "\n"
    save = open("data/save/items_save.txt", "w")
    save.write(items)
    save.close()


def save_game(player):
    inventory = save_player(player)
    save_inventory(inventory)


def read_save_file(file_name):
    save_file = open(file_name, "r")
    read_save = save_file.readlines()
    key_value = [element.strip("\n").split(';')
                 for element in read_save]
    save_file.close()
    return key_value


def build_dict(key_value, inventory=None):
    new_dict = dict()
    for i in range(len(key_value)):
        if key_value[i][1].isdigit():
            new_dict[key_value[i][0]] = int(key_value[i][1])
        elif key_value[i][1] == "" and inventory is not None:
            new_dict[key_value[i][0]] = inventory
        elif key_value[i][1] == "" and inventory is None:
            inventory[key_value[i][0]] = key_value[i][1]
        else:
            new_dict[key_value[i][0]] = key_value[i][1]
    return new_dict


def load_game():
    key_value = read_save_file("data/save/items_save.txt")
    inventory = build_dict(key_value)
    key_value = read_save_file("data/save/player_save.txt")
    player_dict = build_dict(key_value, inventory)
    return player_dict


def play_sound(sound):
    winsound.PlaySound(os.path.dirname(os.path.abspath(
        __file__)) + f'/sounds/{sound}.wav', winsound.SND_ASYNC)
