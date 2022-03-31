import random
from data.monsters_and_npc import journey_project_3, progbasic_exam, journey_project_2, journey_project_1


def step_direction(player, input_char, board):
    illegal_objects = ["#", "K", "W", ">", "<"]
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


def move_monsters(board, turn, level_number):
    if level_number == 1:
        monster_step(board, turn, journey_project_1)
    if level_number == 2:
        monster_step(board, turn, journey_project_2)
    if level_number == 3:
        monster_step(board, turn, journey_project_3)
    if level_number == 4:
        monster_step(board, turn, progbasic_exam)
