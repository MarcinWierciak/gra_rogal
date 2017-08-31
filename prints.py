import visuals


def insert_object(board, x, y, sign): # umieszacza znak na planszy
    board[x][y] = sign
    return board


def print_board(board): # wyświetla planszę z listy board, linia po linii
    for line in board:
        change_color_of_chosen_sign_on_board(line, "·", "G")
        change_color_of_chosen_sign_on_board(line, "~", "S")
        print("".join(line))
    return


def change_color_of_chosen_sign_on_board(lista, chosen_sign, color):
    for element in lista:
        if element == chosen_sign:
            new_element = visuals.change_color(element, color)
            loc = lista.index(element)
            lista.remove(element)
            lista.insert(loc, new_element)


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
        elif counter == 3:
            print_new_string(" "*110, board, 24, 2)
            counter = -1
        counter += 1




def print_new_string(string_to_print, board, x, y):
    counter = 0
    for element in list(str(string_to_print)):
        insert_object(board, x, y+counter, element)
        counter += 1
    return
