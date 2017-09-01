import os
import actions
import mapz
import hero
import move

def main():
    os.system('clear')
    board = mapz.load_map_file("level_1.txt")
    objects =  {"items":["🍶", "🗡", "⛑",], "enemies":["⛇", mapz.change_color("🚹", "R"), "🐲"],
                "actions":["🌑", mapz.change_color("$", "P")],
                "border":[mapz.change_color("#", "O"), mapz.change_color("~", "S")]}
    x, y = 1, 22
    hero_symbol = "♞"
    player = mapz.insert_object(board, x, y, hero_symbol)
    player_stats = hero.choose_character(board)
    move_status = {"coords":[0,0],"action":"", "found_object":""}
    keys = [0,0]

    while True:
        monster_stats = {"hp":130, "dmg":15, "armor":10}
        move_status = move.go_player(board, x, y, objects, player_stats)
        x, y = move_status["coords"]
        action = move_status["action"]
        found_object = move_status["found_object"]
        if action == "fight":
            mapz.print_battle_txt(found_object, board, "start")
            player_stats = actions.fight_result(x, y, board, player_stats, monster_stats)
            mapz.print_battle_txt(found_object, board, "end")

        if action == "chest":
            chest_code = ['1','2','3','2','2','3']
            chest_result = actions.chest(chest_code)
            if chest_result == 1:
                mapz.print_inventory(board, "Dagger", 2.4, ["dmg"], [10], player_stats)
                mapz.print_txt("Znalazłeś Sztylet Zguby, obrażenia zwiększają się o 10. Filetuj!", board)
                mapz.insert_object(board, 1, 19, "·")
            if chest_result == 0:
                mapz.print_txt("Skrzynia zniknęła. Został po niej pył i złe wspomnienie trudnego kodu.", board)
                continue


        if action == "next_level":
            board = found_object

        mapz.print_stats_menu(board, player_stats)
        mapz.insert_object(board, x, y, hero_symbol)
        os.system('clear')
        mapz.print_board(board)


main()
