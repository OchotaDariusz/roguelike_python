

import HeroAndMonsters

player = HeroAndMonsters.player
mercenary = HeroAndMonsters.mercenary
infantry_of_Troy = HeroAndMonsters.infantry_of_Troy
cavalry_of_Troy = HeroAndMonsters.cavalry_of_Troy
enemy_hero = HeroAndMonsters.enemy_hero


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
    damage = attacker["damage"]
    defender["health"] = defender["health"] - damage
    if defender["health"] <= 0:
        print("{} has been slain".format(defender["name"]))
        attacker["xp"] += defender["reward"]
        if attacker == player:
            level_up(attacker)
        else:
            print("Level of {}: {}".format(attacker["name"], attacker["level"]))
        input("Press any key to leave the battle! ")
        exit(0)
    else:
        print("{} has taken {} damage and has {} hp left".format(defender["name"], damage, defender["health"]))


def combat(your_champ, foe):
    print("You have approached {}, if you try to leave now he will stab you in the back to death!".format(foe["name"]))
    while True:
        
        print("------------------------------------------------------------------------")
        decision = input("Do you want to attack or pass your turn? Y = Attack! N = Pass! ").lower()
        if "y" in decision:
            print("------------------------------------------------------------------------")
            deal_damage(your_champ, foe)
            print("-----------------------------------------------------")
            deal_damage(foe, your_champ)
            
        elif "n" in decision:
            print("{} attacks! ".format(foe["name"]))
            print("------------------------------------------------------------------------")
            deal_damage(foe, your_champ)
        else:
            pass

combat(player, mercenary)