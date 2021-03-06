import data.util as util
import data.ascii_art as ascii_art
import random


def print_separator():
    print("-" * 80)


def combat_choice():
    print("\nHere are your choices: \n")
    print("Y: Try to write it slowly (ATTACK)")
    print("S: Use Super Skill (SPELL)")
    print("H: Willpower potion (HP+)")
    print("M: Restores Mana (MP+)")
    print("N: Try to run away")
    print("B: Display your current stats")
    decision = input("\nYour Choice: ").lower()
    return decision


def level_up(character):
    add_str = 0
    add_hp = 0
    add_mana = 0
    while character["xp"] >= character["next_level"]:
        character["level"] += 1
        character["xp"] = character["xp"] - character["next_level"]
        character["next_level"] = round(character["next_level"] * 1.4)
        add_str += 5
        add_hp += 100
        add_mana += 10

    print("level", character["level"])
    print("\nKnowledge(STRENGTH): {} +{} Willpower(HP): {} +{}".format(character["strength"], add_str,
                                                                       character["max_hp"], add_hp))
    character["strength"] += add_str
    character["health"] += add_hp
    character["max_hp"] += add_hp
    character["mana"] += add_mana
    character["max_mana"] += add_mana


def get_skill_damage(attacker):
    if attacker["level"] >= 10 and attacker["mana"] == attacker["max_mana"]:
        attacker["mana"] -= attacker["max_mana"]
        full_damage = (attacker["max_mana"] * 5)
    else:
        print("You need level 10 to cast a spell")
        full_damage = 0
    return full_damage


def get_normal_damage(attacker, defender):
    multiplier = random.randint(60, 100) / 100
    full_damage = int(((attacker["damage"] + int((attacker["strength"] * 0.2))) - defender["armor"]) * multiplier)
    return full_damage


def attack(defender, full_damage):
    defender["health"] = defender["health"] - full_damage


def end_battle(attacker, defender):
    print_separator()
    print("{} has been crushed".format(defender["name"]))
    attacker["xp"] += defender["reward"]
    level_up(attacker)
    max_health_or_mana(attacker)
    print(ascii_art.winner)
    print("Press any key to leave the battle!")
    util.key_pressed()
    if defender["name"] == "Player":
        return None
    return False


def deal_damage(attacker, defender, skill=False):
    if skill:
        full_damage = get_skill_damage(attacker)
    else:
        full_damage = get_normal_damage(attacker, defender)
    attack(defender, full_damage)
    if defender["health"] <= 0:
        return end_battle(attacker, defender)
    if attacker["health"] <= 0:
        return None
    else:
        print("{} has lost {} HP and has {} left after receiving damage".format(
            defender["name"], full_damage, defender["health"]))
        return True


def max_health_or_mana(your_champ):
    if your_champ["health"] >= your_champ["max_hp"]:
        your_champ["health"] = your_champ["max_hp"]
    if your_champ["mana"] >= your_champ["max_mana"]:
        your_champ["mana"] = your_champ["max_mana"]


def use_mana_potions(your_champ):
    if your_champ["inventory"]["mana_potion"] > 0:
        your_champ["mana"] += int(your_champ["max_mana"] * 0.5)
        max_health_or_mana(your_champ)
        your_champ["inventory"]["mana_potion"] -= 1
    else:
        print("You have no more intelligence boost potions!")


def use_healing_potions(your_champ):
    if your_champ["inventory"]["health_potion"] > 0:
        your_champ["health"] += int(your_champ["max_hp"] * 0.3)
        max_health_or_mana(your_champ)
        your_champ["inventory"]["health_potion"] -= 1
    else:
        print("You have no more will power potions!")


def combat(your_champ, foe):
    util.play_sound("fight")
    print_separator()
    print("You have approached {}, if you try to leave now you will fail an exam!".format(foe["name"]))
    print(ascii_art.duel)

    is_combat = True
    while is_combat:
        print()
        print_separator()
        decision = combat_choice()
        util.clear_screen()
        if "y" in decision:
            print_separator()
            is_combat = deal_damage(your_champ, foe)
            if is_combat is False:
                return True
            if is_combat is None:
                return None
            print()
            print_separator()
            is_combat = deal_damage(foe, your_champ)
            if is_combat is False:
                return True
            if is_combat is None:
                return None
        elif "n" in decision:
            print("{} takes its toll! ".format(foe["name"]))
            print_separator()
            is_combat = deal_damage(foe, your_champ)
            if is_combat is False:
                return True
            if is_combat is None:
                return None
        elif "h" in decision:
            use_healing_potions(your_champ)
            print("You have restored {} HP ".format(int(your_champ["max_hp"] * 0.3)))
            print_separator()
            print("\nWillpower(HP) of {} = {}".format(
                your_champ["name"], your_champ["health"]))
            is_combat = deal_damage(foe, your_champ)
            if is_combat is False:
                return True
            if is_combat is None:
                return None
        elif "m" in decision:
            use_mana_potions(your_champ)
            print("Mana restored {} of {}".format(your_champ["max_mana"] * 0.5, your_champ["name"]))
            print_separator()
            print("\nYour current mana level = {} out of {} ".format(
                your_champ["mana"], your_champ["max_mana"]))
            is_combat = deal_damage(foe, your_champ)
            if is_combat is False:
                return True
            if is_combat is None:
                return None
        elif "s" in decision:
            is_combat = deal_damage(your_champ, foe, True)
            if is_combat is False:
                return True
            if is_combat is None:
                return None
        elif "b" in decision:
            print("Your current stats: \nWillpower (HP): {} out of {}\nBrain cells engaged (MANA): {} out of {}".format(
                your_champ["health"], your_champ["max_hp"], your_champ["mana"], your_champ["max_mana"]))
        else:
            pass
