def create_board(width, height):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    pass


def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    pass

ITEM_NAME = 0
ITEM_TYPE = 1
ITEM_DAMAGE = 2
ITEM_DEFENSIVE = 3
ITEM_HEALTH = 4


def read_file(file_name):
    items_table = []
    #item_table structure by index
    #[0] = item name  [1] = type  [2] = damage  [3] = defensive  [4] = health
    text_file = open(file_name , "r")
    for line in text_file:
        items_table.append(line.strip().split("\t"))
    text_file.close()
    return items_table

def add_item_to_player(player,item,items):

    item_type_list = list(player["inventory"].keys())
    if item[ITEM_TYPE] in item_type_list :
        change_item(player,item,items)
    else :
        add_item(player,item)
    

def change_item(player,item,items):
    decide = input("You already have that kind of item, do You want to change it? Y/N  ").upper()
    if decide == "Y" :
        remove_old_item_statistics(player,item,items)
        add_item(player,item)

def add_item(player,item):

    player["damage"] += int(item[ITEM_DAMAGE])
    player["armor"] += int(item[ITEM_DEFENSIVE])    
    player["health"] += int(item[ITEM_HEALTH])
    player["inventory"][item[ITEM_TYPE]] = item[ITEM_NAME]

def remove_old_item_statistics(player,item,items):
    
    for item_name in items :
        if item_name[ITEM_NAME] == player["inventory"][item[ITEM_TYPE]]:
            player["damage"] -= int(item_name[ITEM_DAMAGE])
            player["armor"] -= int(item_name[ITEM_DEFENSIVE]) 
            player["health"] -= int(item_name[ITEM_HEALTH])

"""def change_item(player,item):
    item_type_list = list(player["inventory"].keys())
    if item[ITEM_TYPE] in item_type_list :
        decide = input("You already have that kind of item, do You want to change it? Y/N  ").upper()
        if decide == "Y" :
            player["inventory"][item[ITEM_TYPE]] = item[ITEM_NAME]"""
