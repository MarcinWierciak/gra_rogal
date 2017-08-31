import os
import visuals
import battle
import prints
import terrain
import hero
import move


def lost_game():
    pass


def main():
    board = terrain.read_file("board.txt")
    items = ["🍶", "*", "🗃", "🗡", "⛑"]
    monsters = ["B"]
    border = ["#", visuals.change_color("~", "S")]
    chests = ["1","2","3","4"]
    x, y = 1, 3
    hero_symbol = "K"
    player = terrain.insert_object(board, x, y, hero_symbol)
    goblin = terrain.insert_object(board, 12, 56, "B")
    #terrain.insert_object(board, 12, 12, "🍶")
    #terrain.insert_object(board, 19, 52, "*")
    #terrain.insert_object(board, 13, 44, "⛑")
    #terrain.insert_object(board, 22, 3, "🗡")
    player_stats = hero.choose_character(board)
    monster_stats = {"hp":100, "dmg":10, "armor":8}


    while True:
        move_status = move.go_player(board, x, y, hero_symbol, monsters, items, player_stats, chests)
        x, y = move_status["coords"]
        action = move_status["action"]
        found_object = move_status["found_object"]
        if action == "fight":
            fight_result = battle.fight(board, player_stats, monster_stats)
            while fight_result[0] == 1:
                print(fight_result)
                player_stats["hp"] = "   "
                prints.print_stats_menu(board, player_stats)
                player_stats["hp"] = fight_result[1]
                terrain.insert_object(board, 12, 56, "·")
                break
            lost_game()

        if action == "chest":
            if found_object == "1":
                chest_code = ['1','2','3','2','2','3']
                chest_result = battle.chest(chest_code)
                if chest_result == 1:
                    prints.print_inventory(board, "Dagger", 2.4, ["dmg"], [10], player_stats)
                    prints.print_txt("Znalazłeś sztylet, obrażenia zwiększają się o 10", board)
                    terrain.insert_object(board, 1, 10, "·")

            elif found_object == "2":
                chest_code = ['3','2','1','2','1','3']
                chest_result = battle.chest(chest_code)
                if chest_result == 1:
                    prints.print_inventory(board, "Light armor", 2.4, ["armor"], [10], player_stats)
                    prints.print_txt("Znalazłeś lekka zbroje, armor zwiększa się o 10", board)
                    terrain.insert_object(board, 22, 17, "·")
                
            elif found_object == "3":
                chest_code = ['3','3','3','1','2','1']
                chest_result = battle.chest(chest_code)
                if chest_result == 1:
                    prints.print_inventory(board, "Sword", 2.4, ["dmg"], [15], player_stats)
                    prints.print_txt("Znalazłeś miecz, obrażenia zwiększają się o 15", board)
                    terrain.insert_object(board, 1, 10, "·")

            elif found_object == "4":
                chest_code = ['3','2','2','2','1','2']
                chest_result = battle.chest(chest_code)
                if chest_result == 1:
                    prints.print_inventory(board, "Steel armor", 2.4, ["armor"], [15], player_stats)
                    prints.print_txt("Znalazłeś stalową zbroje, armor zwiększają się o 15", board)
                    terrain.insert_object(board, 1, 10, "·")

            

        prints.print_stats_menu(board, player_stats)
        terrain.insert_object(board, x, y, hero_symbol)
        os.system('clear')
        prints.print_board(board)


main()
