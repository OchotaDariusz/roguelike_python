import data.util as util
import data.ascii_art as ascii_art
import random
import os
import winsound


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
    print("Knowledge: {} +{} Willpower: {} +{}".format(character["strength"], add_str,
                                                       character["max_hp"], add_hp))
    character["strength"] += add_str
    character["health"] += add_hp
    character["max_hp"] += add_hp
    character["max_mana"] += add_mana


def super_ability(your_champ, foe):
    if your_champ["level"] >= 10 and your_champ["mana"] == your_champ["max_mana"]:
        your_champ["mana"] -= your_champ["max_mana"]
        spell_damage = your_champ["max_mana"] * 5 - foe["health"]

        if foe["health"] <= 0:
            print("{} has been finished".format(foe["name"]))
            your_champ["xp"] += foe["reward"]
        else:
            print("{} has progressed by {} points and has {} TODO tasks left".format(
                foe["name"], spell_damage, foe["health"]))
            return True
    elif your_champ["level"] < 10:
        print("Level of your experience is too low to use this skill. Your level {}, required level 10.".format(
            your_champ["level"]))
    elif your_champ["mana"] != your_champ["max_mana"]:
        print("This skill is very draining so it requires engagning every single brain cell, as you are tired drink inteligence boost potion to cast a spell. ")


def deal_damage(attacker, defender):

    multiplier = random.randint(60, 100) / 100
    dealdamage = int(
        ((attacker["damage"] + int((attacker["strength"] * 0.2))) - defender["armor"]) * multiplier)
    if dealdamage <= 0:
        dealdamage = 0
    defender["health"] = defender["health"] - dealdamage

    if defender["health"] <= 0:
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
    if attacker["health"] <= 0:
        return None
    else:
        print("{} has lost {} HP and has {} left after recieving damage".format(
            defender["name"], dealdamage, defender["health"]))
        return True


def max_health_or_mana(your_champ):
    if your_champ["health"] >= your_champ["max_hp"]:
        your_champ["health"] = your_champ["max_hp"]
    elif your_champ["mana"] >= your_champ["max_mana"]:
        your_champ["mana"] = your_champ["max_mana"]


def use_mana_potions(your_champ):
    if your_champ["inventory"]["mana_potion"] > 0:
        your_champ["mana"] += int(your_champ["max_mana"] * 0.5)
        max_health_or_mana(your_champ)
        your_champ["inventory"]["mana_potion"] -= 1
    else:
        print("You have no more inteligence boost potions!")


def use_healing_potions(your_champ):
    if your_champ["inventory"]["health_potion"] > 0:
        your_champ["health"] += int(your_champ["max_hp"] * 0.3)
        max_health_or_mana(your_champ)
        your_champ["inventory"]["health_potion"] -= 1
    else:
        print("You have no more will power potions!")


def combat(your_champ, foe):
    winsound.PlaySound(os.path.dirname(os.path.abspath(
        __file__)) + '/sounds/fight.wav', winsound.SND_ASYNC)
    print("---------------------------------------------------------------------------------")
    print("You have approached {}, if you try to leave now you will fail an exam!".format(
        foe["name"]))
    print(ascii_art.duel)

    is_combat = True
    while is_combat:

        print("\n------------------------------------------------------------------------")
        decision = input("\nHere are your choices: \n\nY: You try to write it slowly\n\n\nN: You try to run away because it's too hard but you can't escape your destiny so it decreases your willpower and forces you to proceed to it anyway\n\n\nH: You use potion that is going to increase your willpower(HP) so if you are lucky enough you will handle an exam\n\n\nM: Dring mighty intelligence booster to use all of your brain cells on a given task\n\n\nS: If you are sufficiently commited in the task you can use your super power to crush any module or exam\n\n\nB: Display your current stats such as HP or MANA(brain cells engaged)\n\nYour Choice: ").lower()
        util.clear_screen()
        if "y" in decision:
            print(
                "------------------------------------------------------------------------")
            is_combat = deal_damage(your_champ, foe)
            if is_combat is False:
                return True
            if is_combat is None:
                return None
            print(
                "\n------------------------------------------------------------------------")
            is_combat = deal_damage(foe, your_champ)
            if is_combat is False:
                return True
            if is_combat is None:
                return None
        elif "n" in decision:
            print("{} takes its toll! ".format(foe["name"]))
            print(
                "------------------------------------------------------------------------")
            is_combat = deal_damage(foe, your_champ)
            if is_combat is False:
                return True
            if is_combat is None:
                return None

        elif "h" in decision:
            use_healing_potions(your_champ)
            print("You have restored {} HP but you also lost some coz of elevated stress level ".format(
                int(your_champ["max_hp"] * 0.3)))
            print(
                "---------------------------------------------------------------------------")
            print("\nHP of {} after using willpower potion = {}".format(
                your_champ["name"], your_champ["health"]))
            is_combat = deal_damage(foe, your_champ)
            if is_combat is False:
                return True
            if is_combat is None:
                return None
        elif "m" in decision:
            use_mana_potions(your_champ)
            print("Inteligence booster fires up to {} billion neurons of {}".format(
                your_champ["max_mana"] * 0.5, your_champ["name"]))
            print(
                "------------------------------------------------------------------------")
            print("\nYour brain has engaged {} out of {} billion neurons into task. ".format(
                your_champ["mana"], your_champ["max_mana"]))
            is_combat = deal_damage(foe, your_champ)
            if is_combat is False:
                return True
            if is_combat is None:
                return None
        elif "s" in decision:
            super_ability(your_champ, foe)
            is_combat = deal_damage(foe, your_champ)
            if is_combat is False:
                return True
            if is_combat is None:
                return None
        elif "b" in decision:
            print("Your current stats: \nWillpower(HP): {} out of {}\nBrain cells engaged: {} out of {}".format(
                your_champ["health"], your_champ["max_hp"], your_champ["mana"], your_champ["max_mana"]))

        else:
            pass
