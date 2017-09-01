import csv
import os

def load_map_file(filename):
    board = []
    complete_board = []
    with open(filename, newline='') as inputfile:
        for row in csv.reader(inputfile):
            board.append(row)
    for element in board:
        complete_board.append(list(element[0]))
    return complete_board


def insert_object(board, x, y, sign): # umieszacza znak na planszy
    board[x][y] = sign
    return board


def print_board(board):
    for line in board:
        change_color_of_chosen_sign_on_board(line, "·", "G")
        change_color_of_chosen_sign_on_board(line, "~", "S")
        change_color_of_chosen_sign_on_board(line, "🚹", "R")
        change_color_of_chosen_sign_on_board(line, "#", "O")
        change_color_of_chosen_sign_on_board(line, "$", "P")
        print("".join(line))
    return


def change_color_of_chosen_sign_on_board(lista, chosen_sign, color):
    for element in lista:
        if element == chosen_sign:
            new_element = change_color(element, color)
            loc = lista.index(element)
            lista.remove(element)
            lista.insert(loc, new_element)


def change_color(string, color):
    if color == 'W':
        colored_string = '\033[0m' + string + '\033[0m' # white (normal)
    if color == 'R':
        colored_string = '\033[31m' + string + '\033[0m' # red
    if color == 'G':
        colored_string = '\033[32m' + string + '\033[0m' # green
    if color == 'O':
        colored_string = '\033[33m' + string + '\033[0m' # orange
    if color == 'B':
        colored_string = '\033[34m' + string + '\033[0m' # blue
    if color == 'P':
        colored_string = '\033[35m' + string + '\033[0m' # purple
    if color == 'S':
        colored_string = '\033[36m' + string + '\033[0m' # sea blue
    return colored_string


def print_stats_menu(board, player_stats):
    print_new_string(player_stats["name"], board, 1, 104)
    print_new_string(player_stats["h_class"], board, 2, 104)
    print_new_string(player_stats["hp"], board, 6, 104)
    print_new_string(player_stats["dmg"], board, 7, 104)
    print_new_string(player_stats["armor"], board, 9, 104)
    print_new_string(player_stats["int"], board, 10, 104)
    print_new_string(player_stats["str"], board, 8, 104)
    return


def print_inventory(board, item, weigth, chosen_stat, extra_value_of_stat, player_stats): # chosen_stat i extra_value_of_stat muszą być listą!
    place_counter = 0
    stat_counter = len(chosen_stat)
    while True:
        if board[14+place_counter][98] == " ":
            print_new_string(item, board, 14+place_counter, 98)
            print_new_string(weigth, board, 14+place_counter, 112)
            while stat_counter > 0:
                player_stats[chosen_stat[stat_counter-1]] += extra_value_of_stat[stat_counter-1]
                print_stats_menu(board, player_stats)
                stat_counter -= 1
            return

        place_counter += 1


def print_txt(message, board):
    counter = 0
    while True:
        if board[24+counter][2] == " ":
            print_new_string(message, board, 24+counter, 2)
            return
        elif counter == 4:
            print_new_string(" "*110, board, 24, 2)
            counter = -1
        counter += 1


def print_battle_txt(found_object, board, battle_status):
    if found_object == "⛇" and battle_status == "start":
        print_txt("Mostu broni olbrzymi śnieżny troll. Zdołasz go zabić przed wiosną?", board)
    if found_object == "⛇" and battle_status == "end":
        print_txt("'Giń kupo wody, wracaj gdzie twe miejsce - pod most.' Droga wolna.", board)
    elif found_object == change_color("🚹", "R") and battle_status == "start":
        print_txt("Czerwonawy Typ z Hakiem broni tego przejścia. Sprawdźmy jaki z niego Crag Hack.", board)
    elif found_object == change_color("🚹", "R") and battle_status == "end":
        print_txt("'Hak wylądował tam gdzie jego miejsce, mówcie mi Kuba Rozhaczacz.'", board)
    elif found_object == "🐲" and battle_status == "start":
        print_txt("'Wreszcie ta gra nabiera trudności, smok... wielkości osła? Co jeszcze? Galactus wielkości mrówki?'", board)
    elif found_object == "🐲" and battle_status == "start":
        print_txt("'Hm, w świecie fantasy smokobójcom można wszystko. Zamek, księżniczkę i hamburgera proszę. Dwa razy.'", board)
    return



def print_new_string(string_to_print, board, x, y):
    counter = 0
    for element in list(str(string_to_print)):
        insert_object(board, x, y+counter, element)
        counter += 1
    os.system('clear')
    print_board(board)
    return
