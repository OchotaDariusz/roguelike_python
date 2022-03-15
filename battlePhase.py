
def level_up(character):
    add_str = 0
    add_hp = 0
    while character["xp"] >= character["next_level"]:
        character["level"] += 1
        character["xp"] = character["xp"] - character["next_level"]
        character["next_level"] = round(character["next_level"] * 1.4)
        add_str += 5
        add_hp += 100

    print("level", character["level"])
    print("Strength: {} +{} Health Points: {} +{}".format(character["strength"], add_str,
                                                          character["health"], add_hp))
    character["strength"] += add_str
    character["health"] += add_hp


def deal_damage(attacker, defender):
    print(attacker["damage"])
    print(defender["health"])
    defender["health"] = defender["health"] - attacker["damage"]
    if defender["health"] <= 0:
        print("{} has been slain".format(defender["name"]))
        attacker["xp"] += defender["reward"]
        level_up(attacker)
        input("Press any key to leave the battle! ")
        return False
    else:
        print("{} has taken {} damage and has {} hp left".format(defender["name"], attacker["damage"], defender["health"]))
        return True

def combat(your_champ, foe):
    print("You have approached {}, if you try to leave now he will stab you in the back to death!".format(foe["name"]))
    is_combat = True
    while is_combat:
        
        print("------------------------------------------------------------------------")
        decision = input("Do you want to attack or pass your turn? Y = Attack! N = Pass! ").lower()
        if "y" in decision:
            print("------------------------------------------------------------------------")
            is_combat = deal_damage(your_champ, foe)
            print("-----------------------------------------------------")
            is_combat = deal_damage(foe, your_champ)
            
        elif "n" in decision:
            print("{} attacks! ".format(foe["name"]))
            print("------------------------------------------------------------------------")
            is_combat = deal_damage(foe, your_champ)
        else:
            pass