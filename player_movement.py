import msvcrt
import sys


def step_direction(player, input_char, board):
    while True:
        can_move = True
        if input_char.upper() == 'W':
            if player["type"] == 'boss':
                for i in range(5):
                    if board[player["pos_x"] - 1][player["pos_y"] + i] == "#" or \
                       board[player["pos_x"] - 1][player["pos_y"] + i] == "M" or \
                       board[player["pos_x"] - 1][player["pos_y"] + i] == "I":
                        can_move = False
                        break
            if player["type"] == 'monster':
                if board[player["pos_x"] - 1][player["pos_y"]] == "#" or \
                   board[player["pos_x"] - 1][player["pos_y"]] == "M" or \
                   board[player["pos_x"] - 1][player["pos_y"]] == "I" or \
                   board[player["pos_x"] - 1][player["pos_y"]] == "B" or \
                   board[player["pos_x"] - 1][player["pos_y"]] == "^" or \
                   board[player["pos_x"] - 1][player["pos_y"]] == "V" or \
                   board[player["pos_x"] - 1][player["pos_y"]] == "<" or \
                   board[player["pos_x"] - 1][player["pos_y"]] == ">":
                    can_move = False
            elif player["type"] == 'player' and board[player["pos_x"] - 1][player["pos_y"]] == "#":
                can_move = False
            if can_move:
                player["pos_x"] = player["pos_x"] - 1
            break
        elif input_char.upper() == 'S':
            if player["type"] == 'boss':
                for i in range(5):
                    if board[player["pos_x"] + 5][player["pos_y"] + i] == "#" or \
                       board[player["pos_x"] + 5][player["pos_y"] + i] == "M" or \
                       board[player["pos_x"] + 5][player["pos_y"] + i] == "I":
                        can_move = False
                        break
            if player["type"] == 'monster':
                if board[player["pos_x"] + 1][player["pos_y"]] == "#" or \
                   board[player["pos_x"] + 1][player["pos_y"]] == "M" or \
                   board[player["pos_x"] + 1][player["pos_y"]] == "I" or \
                   board[player["pos_x"] + 1][player["pos_y"]] == "B" or \
                   board[player["pos_x"] + 1][player["pos_y"]] == "^" or \
                   board[player["pos_x"] + 1][player["pos_y"]] == "V" or \
                   board[player["pos_x"] + 1][player["pos_y"]] == "<" or \
                   board[player["pos_x"] + 1][player["pos_y"]] == ">":
                    can_move = False
            elif player["type"] == 'player' and board[player["pos_x"] + 1][player["pos_y"]] == "#":
                can_move = False
            if can_move:
                player["pos_x"] = player["pos_x"] + 1
            break
        elif input_char.upper() == 'A':
            if player["type"] == 'boss':
                for i in range(5):
                    if board[player["pos_x"] + i][player["pos_y"] - 1] == "#" or \
                       board[player["pos_x"] + i][player["pos_y"] - 1] == "M" or \
                       board[player["pos_x"] + i][player["pos_y"] - 1] == "I":
                        can_move = False
                        break
            if player["type"] == 'monster':
                if board[player["pos_x"]][player["pos_y"] - 1] == "#" or \
                   board[player["pos_x"]][player["pos_y"] - 1] == "M" or \
                   board[player["pos_x"]][player["pos_y"] - 1] == "I" or \
                   board[player["pos_x"]][player["pos_y"] - 1] == "B" or \
                   board[player["pos_x"]][player["pos_y"] - 1] == "^" or \
                   board[player["pos_x"]][player["pos_y"] - 1] == "V" or \
                   board[player["pos_x"]][player["pos_y"] - 1] == "<" or \
                   board[player["pos_x"]][player["pos_y"] - 1] == ">":
                    can_move = False
            elif player["type"] == 'player' and board[player["pos_x"]][player["pos_y"] - 1] == "#":
                can_move = False
            if can_move:
                player["pos_y"] = player["pos_y"] - 1
            break
        elif input_char.upper() == 'D':
            if player["type"] == 'boss':
                for i in range(5):
                    if board[player["pos_x"] + i][player["pos_y"] + 5] == "#" or \
                       board[player["pos_x"] + i][player["pos_y"] + 5] == "M" or \
                       board[player["pos_x"] + i][player["pos_y"] + 5] == "I":
                        can_move = False
                        break
            if player["type"] == 'monster':
                if board[player["pos_x"]][player["pos_y"] + 1] == "#" or \
                   board[player["pos_x"]][player["pos_y"] + 1] == "M" or \
                   board[player["pos_x"]][player["pos_y"] + 1] == "I" or \
                   board[player["pos_x"]][player["pos_y"] + 1] == "B" or \
                   board[player["pos_x"]][player["pos_y"] + 1] == "^" or \
                   board[player["pos_x"]][player["pos_y"] + 1] == "V" or \
                   board[player["pos_x"]][player["pos_y"] + 1] == "<" or \
                   board[player["pos_x"]][player["pos_y"] + 1] == ">":
                    can_move = False
            elif player["type"] == 'player' and board[player["pos_x"]][player["pos_y"] + 1] == "#":
                can_move = False
            if can_move:
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
