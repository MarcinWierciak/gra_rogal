import mapz


def choose_character(board):
    player_stats = {"name":"", "h_class":"", "hp":0, "dmg":0, "armor":0, "int":0, "str":0}
    player_name = input("Enter your name: ")
    while True:
        player_class = input("Choose class:\n k = KNIGHT\n b = BARBARIAN\n w = WARRIOR\n h = HUNTER\n")
        if player_class == "k":
            player_stats.update(name=player_name, h_class="Knight", hp=120, dmg=14, armor=12, int=7, str=6)
        elif player_class == "b":
            player_stats.update(name=player_name, h_class="Barbarian", hp=110, dmg=22, armor=5, int=3, str=10)
        elif player_class == "w":
            player_stats.update(name=player_name, h_class="Warrior", hp=100, dmg=16, armor=9, int=5, str=8)
        elif player_class == "h":
            player_stats.update(name=player_name, h_class="Hunter", hp=90, dmg=20, armor=7, int=9, str=5)
        else:
            print("Choose correct class!")
            continue
        mapz.print_stats_menu(board, player_stats)
        break

    return player_stats


def add_item(board, added_item, player_stats):
    if added_item == "🍶":
        mapz.print_inventory(board, "Potion", 0.1, ["hp"], [50], player_stats)
        mapz.print_txt("Znalazłeś butelkę wina 'Życidajka', otrzymujesz +50 HP. Na zdrowie!", board)

    elif added_item == "🔑":
        mapz.print_inventory(board, "Diamond", 0.2, ["str"], [1], player_stats)
        mapz.print_txt("'Drewaniany klucz? Hm, pewnie do drewanianych drzwi.'", board)
        keys = [1,0]

    elif added_item == "⛑":
        mapz.print_inventory(board, "Holy Helm", 1.1, ["int", "armor"], [1, 2], player_stats)
        mapz.print_txt("Holy Helm jest Twój. Zakonnice Pytona latami nad nim klęczały, byś dostał: INT +1, ARMOR +2. Amen!", board)

    elif added_item == "🗡":
        mapz.print_inventory(board, "Silver Sword", 1.4, ["dmg"], [4], player_stats)
        mapz.print_txt("Żaden wampir już nie będzię przyssawał się do Twej aorty. Srebny Miecz podwyższa obrażenia o 4", board)

    return


def lost_game():
    raise SystemExit("You are DEAD.")
