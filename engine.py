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
    
    compare_items(player,item,items)
    decide = input("\n\nDo You want to change current item? Y/N  ").upper()
    while decide not in ["Y","N"]:
        decide = input("please type 'Y' or 'N'  ").upper()
    if decide == "Y" :
        remove_old_item_statistics(player,item,items)
        add_item(player,item)
    elif decide == "N" :
        pass

def add_item(player,item):

    player["damage"] += int(item[ITEM_DAMAGE])
    player["armor"] += int(item[ITEM_DEFENSIVE])    
    player["health"] += int(item[ITEM_HEALTH])
    player["inventory"][item[ITEM_TYPE]] = item[ITEM_NAME]

def remove_old_item_statistics(player,item,items):
    
    for old_item in items :
        if old_item[ITEM_NAME] == player["inventory"][item[ITEM_TYPE]]:
            player["damage"] -= int(old_item[ITEM_DAMAGE])
            player["armor"] -= int(old_item[ITEM_DEFENSIVE]) 
            player["health"] -= int(old_item[ITEM_HEALTH])

def compare_items(player,item,items):
    print("You already have that kind of item\n")
    details_label = ["name:","type:","damage:","defense:","health:"]
    for old_item in items :
         if old_item[ITEM_NAME] == player["inventory"][item[ITEM_TYPE]]:
             print("old item details: ")
             for i in range(len(old_item)):
                 print(details_label[i],old_item[i],end="  ")
    print("\n\nnew item details:")
    for i in range(len(item)):
        print(details_label[i],item[i],end="  ")

def show_inventory(player,items):
    details_label = ["name:","type:","damage:","defense:","health:"]
    player_items_name_list = list(player["inventory"].values())
    print("Your inventory:\n")
    for item_name in player_items_name_list :           
        for i in range(len(items[0])) :
            if item_name == items[i][ITEM_NAME] :
                for j in range(len(items[i])):
                    print(details_label[j],items[i][j])
                print()    
