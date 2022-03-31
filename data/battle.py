from pytest import PytestAssertRewriteWarning
import data.util as util
import data.ascii_art as ascii_art
import random
import os
import winsound


def level_up(character):
    add_str = 0
    add_hp = 0
    while character["xp"] >= character["next_level"]:
        character["level"] += 1
        character["xp"] = character["xp"] - character["next_level"]
        character["next_level"] = round(character["next_level"] * 1.4)
        add_str += 5
        add_hp += 100
        add_mana += 10

    print("level", character["level"])
    print("Strength: {} +{} Health Points: {} +{}".format(character["strength"], add_str,
                                                          character["maxHP"], add_hp))
    character["strength"] += add_str
    character["health"] += add_hp
    character["maxHP"] += add_hp
    character["maxMana"] += add_mana


def super_ability(your_champ, foe):
    if your_champ["level"] >= 10 and your_champ["mana"] == your_champ["maxMana"]:
        your_champ["mana"] -= your_champ["maxMana"]
        spell_damage = foe["health"] - your_champ["maxMana"] * 5
        if foe["health"] <= 0:
            print("{} has been finished".format(foe["name"]))
            your_champ["xp"] += foe["reward"]
        else:
            print("{} has progressed by {} points and has {} TODO tasks left".format(
                foe["name"], spell_damage, foe["health"]))
            return True  
    elif your_champ["level"] < 10:
        print("Level of your experience is too low to use this skill. Your level {}, required level 12.".format(your_champ["level"]))
    elif your_champ["mana"] != your_champ["maxMana"]:
        print("This skill is very draining so it requires every single mana point, as you dont have full mana bar you cannot cast the spell. ")


def deal_damage(attacker, defender):

    multiplier = random.randint(60, 100) / 100
    dealdamage = int(
        ((attacker["damage"] + int((attacker["strength"] * 0.2))) - defender["armor"]) * multiplier)
    if dealdamage <= 0:
        dealdamage = 0
    defender["health"] = defender["health"] - dealdamage

    if defender["health"] <= 0:
        print("{} has been slain".format(defender["name"]))
        attacker["xp"] += defender["reward"]
        level_up(attacker)
        max_health(attacker)
        print(ascii_art.winner)
        print("Press any key to leave the battle!")
        util.key_pressed()
        if defender["name"] == "Player":
            return None
        return False
    if attacker["health"] <= 0:
        return None
    else:
        print("{} has taken {} damage and has {} hp left".format(
            defender["name"], dealdamage, defender["health"]))
        return True


def max_and_min_mana():
    pass


def max_health(your_champ):
    if your_champ["health"] >= your_champ["maxHP"]:
        your_champ["health"] = your_champ["maxHP"]

def use_mana_potions():
    PytestAssertRewriteWarning

def use_healing_potions(your_champ):
    if your_champ["inventory"]["potion"] > 0:
        your_champ["health"] += int(your_champ["maxHP"] * 0.3)
        max_health(your_champ)
        your_champ["inventory"]["potion"] -= 1
    else:
        print("You have no more potions!")
    

def combat(your_champ, foe):
    winsound.PlaySound(os.path.dirname(os.path.abspath(
        __file__)) + '/sounds/fight.wav', winsound.SND_ASYNC)
    print("You have approached {}, if you try to leave now he will stab you in the back to death!".format(
        foe["name"]))
    print(ascii_art.duel)

    is_combat = True
    while is_combat:

        print("------------------------------------------------------------------------")
        decision = input(
            "Do you want to attack or pass your turn? Y = Attack! N = Pass! H = Heal! ").lower()
        util.clear_screen()
        if "y" in decision:
            print(
                "------------------------------------------------------------------------")
            is_combat = deal_damage(your_champ, foe)
            if is_combat is False:
                return True
            if is_combat is None:
                return None
            print("-----------------------------------------------------")
            is_combat = deal_damage(foe, your_champ)
            if is_combat is False:
                return True
            if is_combat is None:
                return None
        elif "n" in decision:
            print("{} attacks! ".format(foe["name"]))
            print(
                "------------------------------------------------------------------------")
            is_combat = deal_damage(foe, your_champ)
            if is_combat is False:
                return True
            if is_combat is None:
                return None
        elif "h" in decision:
            use_potions(your_champ)
            print("You have restored {} hp but you have been hit while drinking potion ".format(
                int(your_champ["maxHP"] * 0.3)))
            print("Hp of {} = {}".format(
                your_champ["name"], your_champ["health"]))
            is_combat = deal_damage(foe, your_champ)
            if is_combat is False:
                return True
            if is_combat is None:
                return None
        elif "s" in decision:
            super_ability(your_champ, foe)
            is_combat = deal_damage(foe, your_champ)

        else:
            pass
