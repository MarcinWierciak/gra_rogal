import random
import time
import os
import prints


############# COLORS FOR STRINGS ############
W = '\033[0m'  # white (normal)
R = '\033[31m' # red
G = '\033[32m' # green



def fight(board, player_stats, monster_stats):
    battle_result = []
    while True:
        counter = 0
        while counter < 6:
            if player_stats["hp"] <= 0 or monster_stats["hp"] <= 0:
                break
            else:
                counter += 1
                monster_stats["hp"], player_stats["hp"] = deal_damages(player_stats, monster_stats)

        if player_stats["hp"] <= 0:
            battle_result.append(0)
            return battle_result

        elif monster_stats["hp"] <= 0:
            print("You win !")
            time.sleep(1)
            battle_result.extend((1, player_stats["hp"]))
            return battle_result

        os.system('clear')
        prints.print_board(board)


def deal_damages(player_stats, monster_stats):
    time.sleep(0.5)
    actual_player_dmg = int((player_stats["dmg"] * random.uniform(0.5, 0.8)) / (monster_stats["armor"] * random.uniform(0.1, 0.3)))
    monster_stats["hp"] = monster_stats["hp"] - actual_player_dmg
    print("{}You deal {} damage {}({} HP ){}".format(G , actual_player_dmg, R, monster_stats["hp"], W))
    time.sleep(0.5)
    actual_monster_dmg = int((monster_stats["dmg"] * random.uniform(0.5, 0.8)) / (player_stats["armor"] * random.uniform(0.1, 0.3)))
    player_stats["hp"] = player_stats["hp"] - actual_monster_dmg
    print("{}You are hit by monster with {} damage {}( {} HP){}".format(R,  actual_monster_dmg, G, player_stats["hp"], W))
    return monster_stats["hp"], player_stats["hp"]


def chest(chest_code):

    chest_result = 0

    while True:

        hints = []
        guess = input("Open a chest by entering a combination of 1\'s, 2\'s, 3\s (6 numbers):")

        if guess.isdigit() and len(guess) == 6:

            guess = list(guess)

            if guess == chest_code:
                chest_result = 1
                print("You opened a chest !")
                return chest_result

            for i in range(len(guess)):
                if guess[i] == chest_code[i]:
                    hints.insert(i,'OK')
                else:
                    hints.insert(i, 'bad')

            print(hints)
            time.sleep(0.5)

            question = input("Do you want to try again? Y or N: ")
            if question.lower == "y":
                continue
            elif question.lower == "n":
                chest_result = 0
                return chest_result
            else:
                continue


        else:
            print('Combination should be 6-digit!')
            continue
