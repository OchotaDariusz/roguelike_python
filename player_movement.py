import msvcrt
import sys


def step_direction(player, input_char, board):

    while True:
        if input_char.upper() == 'W':
            if board[player["pos_x"] - 1][player["pos_y"]] == "#":
                break
            else:
                player["pos_x"] = player["pos_x"] - 1
                break
        elif input_char.upper() == 'S':
            if board[player["pos_x"] + 1][player["pos_y"]] == "#":
                break
            else:
                player["pos_x"] = player["pos_x"] + 1
                break
        elif input_char.upper() == 'A':
            if board[player["pos_x"]][player["pos_y"] - 1] == "#":
                break
            else:
                player["pos_y"] = player["pos_y"] - 1
                break
        elif input_char.upper() == 'D':
            if board[player["pos_x"]][player["pos_y"] + 1] == "#":
                break
            else:
                player["pos_y"] = player["pos_y"] + 1
                break
        else:
            input_char = msvcrt.getwch()
            if input_char == 'q':
                sys.exit()


def step_on_item(player, item):

    if player["pos_x"] == item["pos_x"] and player["pos_y"] == item["pos_y"]:
        # funkcja pobierająca item
        print("dupa")


def step_on_monster(player, monster):

    if player["pos_x"] == monster["pos_x"] and player["pos_y"] == monster["pos_y"]:
        # tryb walki
        print("monster")
