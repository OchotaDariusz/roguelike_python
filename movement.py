import random
from monsters import cavalry_of_troy, enemy_hero, infantry_of_troy, mercenary


def step_direction(player, input_char, board):
    illegal_objects = ["#", "M", "I", "C", "T", "B", ">", "<"]
    can_move = True
    if input_char.upper() == 'W':
        if player["type"] == 'boss':
            for i in range(5):
                if board[player["pos_x"] - 1][player["pos_y"] + i] in illegal_objects:
                    can_move = False
        if player["type"] == 'monster':
            if board[player["pos_x"] - 1][player["pos_y"]] in illegal_objects:
                can_move = False
        elif player["type"] == 'player' and \
                board[player["pos_x"] - 1][player["pos_y"]] == "#":
            can_move = False
        if can_move:
            player["pos_x"] = player["pos_x"] - 1

    elif input_char.upper() == 'S':
        if player["type"] == 'boss':
            for i in range(5):
                if board[player["pos_x"] + 5][player["pos_y"] + i] in illegal_objects:
                    can_move = False
        if player["type"] == 'monster':
            if board[player["pos_x"] + 1][player["pos_y"]] in illegal_objects:
                can_move = False
        elif player["type"] == 'player' and \
                board[player["pos_x"] + 1][player["pos_y"]] == "#":
            can_move = False
        if can_move:
            player["pos_x"] = player["pos_x"] + 1

    elif input_char.upper() == 'A':
        if player["type"] == 'boss':
            for i in range(5):
                if board[player["pos_x"] + i][player["pos_y"] - 1] in illegal_objects:
                    can_move = False
        if player["type"] == 'monster':
            if board[player["pos_x"]][player["pos_y"] - 1] in illegal_objects:
                can_move = False
        elif player["type"] == 'player' and \
                board[player["pos_x"]][player["pos_y"] - 1] == "#":
            can_move = False
        if can_move:
            player["pos_y"] = player["pos_y"] - 1

    elif input_char.upper() == 'D':
        if player["type"] == 'boss':
            for i in range(5):
                if board[player["pos_x"] + i][player["pos_y"] + 5] in illegal_objects:
                    can_move = False
        if player["type"] == 'monster':
            if board[player["pos_x"]][player["pos_y"] + 1] in illegal_objects:
                can_move = False
        elif player["type"] == 'player' and \
                board[player["pos_x"]][player["pos_y"] + 1] == "#":
            can_move = False
        if can_move:
            player["pos_y"] = player["pos_y"] + 1


def monster_step(board, turn, enemy):
    if enemy["is_alive"] and turn % 2 == 0:
        rand_key = random.choice(["W", "S", "D", "A"])
        step_direction(enemy, rand_key, board)


def move_monsters(board, turn):
    monsters = [mercenary, infantry_of_troy, cavalry_of_troy, enemy_hero]
    for monster in monsters:
        monster_step(board, turn, monster)
