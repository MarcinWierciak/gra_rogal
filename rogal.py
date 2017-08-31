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
        if move.go_player(board, x, y, hero_symbol, monsters, items, player_stats, chests)["action"] == "fight":
            fight_result = battle.fight(board, player_stats, monster_stats)
            while fight_result[0] == 1:
                print(fight_result)
                player_stats["hp"] = "   "
                prints.print_stats_menu(board, player_stats)
                player_stats["hp"] = fight_result[1]
                terrain.insert_object(board, 12, 56, "·")
                break
            lost_game()

        if move.go_player(board, x, y, hero_symbol, monsters, items, player_stats, chests)["action"] == "chest": 

            if move.go_player(board, x, y, hero_symbol, monsters, items, player_stats, chests)["found_object"] == "1":
                chest_code = ['1','2','3','2','2','3']
                chest_result = battle.chest(chest_code)
                if chest_result == 1:
                    prints.print_inventory(board, "Dagger", 2.4, ["dmg"], [10], player_stats)
                    prints.print_txt("Znalazłeś sztylet, obrażenia zwiększają się o 10", board)
                    terrain.insert_object(board, 1, 10, "·")


        prints.print_stats_menu(board, player_stats)
        x = move.go_player(board, x, y, hero_symbol, monsters, items, player_stats, chests)["x_coord"]
        y = move.go_player(board, x, y, hero_symbol, monsters, items, player_stats, chests)["y_coord"]
        terrain.insert_object(board, x, y, hero_symbol)
        os.system('clear')
        prints.print_board(board)


main()
